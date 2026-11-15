"""Organisation A: one self-contained script."""
from datetime import date, timedelta
from pathlib import Path

records = [
    ("192311001", "2026-10-01", "A"),
    ("192311001", "2026-10-02", "A"),
    ("192311001", "2026-10-03", "A"),
    ("192311002", "2026-10-01", "P"),
    ("192311002", "2026-10-02", "A"),
    ("192311002", "2026-10-03", "A"),
    ("192311003", "2026-10-01", "A"),
    ("192311003", "2026-10-02", "P"),
    ("192311003", "2026-10-03", "A"),
]


def find_three_day_absences(rows):
    by_student = {}
    for reg_no, day_text, status in rows:
        by_student.setdefault(reg_no, []).append((date.fromisoformat(day_text), status))
    result = []
    for reg_no, entries in by_student.items():
        entries.sort()
        run = 0
        previous = None
        for day, status in entries:
            if status == "A" and (previous is None or day == previous + timedelta(days=1)):
                run += 1
            elif status == "A":
                run = 1
            else:
                run = 0
            previous = day
            if run >= 3:
                result.append(reg_no)
                break
    return result


def write_report(rows):
    output = Path(__file__).parent / "output"
    output.mkdir(exist_ok=True)
    result = find_three_day_absences(rows)
    (output / "three_day_absent.txt").write_text(
        "\n".join(result) + ("\n" if result else ""), encoding="utf-8")
    print("Three consecutive absence list:", result)


if __name__ == "__main__":
    write_report(records)
