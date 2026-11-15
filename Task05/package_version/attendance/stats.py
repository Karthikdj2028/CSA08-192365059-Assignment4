"""Calculate attendance statistics."""
from datetime import date, timedelta


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
            if streak >= 3:
                result.append(reg_no)
                break
    return result
