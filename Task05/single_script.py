"""One script: read attendance, calculate percentages and find 3-day absences."""
import csv
from datetime import date, timedelta
from pathlib import Path

BASE = Path(__file__).parent


def main():
    records = []
    with open(BASE / "input" / "attendance.csv", "r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            if row["status"] in ("P", "A"):
                records.append((row["reg_no"], date.fromisoformat(row["date"]), row["status"]))

    counts = {}
    days = {}
    for reg_no, day, status in records:
        counts.setdefault(reg_no, {"P": 0, "A": 0})
        counts[reg_no][status] += 1
        days.setdefault(reg_no, []).append((day, status))

    percentages = {}
    for reg_no, value in counts.items():
        total = value["P"] + value["A"]
        percentages[reg_no] = value["P"] / total * 100

    absentees = []
    for reg_no, entries in days.items():
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
                absentees.append(reg_no)
                break

    output = BASE / "output"
    output.mkdir(exist_ok=True)
    with open(output / "attendance_summary.txt", "w", encoding="utf-8") as file:
        for reg_no, pct in sorted(percentages.items()):
            file.write(f"{reg_no}: {pct:.2f}%\n")
    with open(output / "three_day_absent.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(absentees))
    print("Attendance percentages:", percentages)
    print("Absent for three consecutive days:", absentees)


if __name__ == "__main__":
    main()
