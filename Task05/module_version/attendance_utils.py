"""Reusable attendance functions for the one-module organisation."""
from datetime import date, timedelta
from pathlib import Path

RECORDS = [
    ("192311001", "2026-10-01", "A"),
    ("192311001", "2026-10-02", "A"),
    ("192311001", "2026-10-03", "A"),
    ("192311002", "2026-10-01", "P"),
    ("192311002", "2026-10-02", "A"),
    ("192311002", "2026-10-03", "A"),
]


def three_day_absentees(rows):
    by_student = {}
    for reg_no, day_text, status in rows:
        by_student.setdefault(reg_no, []).append((date.fromisoformat(day_text), status))
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
            if streak == 3:
                result.append(reg_no)
                break
    return result


def save_report(rows, output_file):
    result = three_day_absentees(rows)
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    Path(output_file).write_text("\n".join(result), encoding="utf-8")
    return result
