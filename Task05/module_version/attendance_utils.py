"""One reusable module for reading attendance and writing two reports."""
import csv
from datetime import date, timedelta
from pathlib import Path


def read_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            if row["status"] in ("P", "A"):
                records.append((row["reg_no"], date.fromisoformat(row["date"]), row["status"]))
    return records


def attendance_percentages(records):
    counts = {}
    for reg_no, day, status in records:
        counts.setdefault(reg_no, {"P": 0, "A": 0})
        counts[reg_no][status] += 1
    return {
        reg_no: value["P"] / (value["P"] + value["A"]) * 100
        for reg_no, value in counts.items()
    }


def three_day_absentees(records):
    by_student = {}
    for reg_no, day, status in records:
        by_student.setdefault(reg_no, []).append((day, status))
    result = []
    for reg_no, entries in by_student.items():
        entries.sort()
        streak = 0
        previous = None
        for day, status in entries:
            if status == "A" and (previous is None or day == previous + timedelta(days=1)):
                streak += 1
            elif status == "A":
                streak = 1
            else:
                streak = 0
            previous = day
            if streak >= 3:
                result.append(reg_no)
                break
    return result


def write_reports(percentages, absentees, output_folder):
    output = Path(output_folder)
    output.mkdir(parents=True, exist_ok=True)
    with open(output / "attendance_summary.txt", "w", encoding="utf-8") as file:
        for reg_no, value in sorted(percentages.items()):
            file.write(f"{reg_no}: {value:.2f}%\n")
    with open(output / "three_day_absent.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(sorted(absentees)))
