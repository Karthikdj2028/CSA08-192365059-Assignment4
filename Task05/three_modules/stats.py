"""Statistics module: calculate percentages and consecutive absences."""
from datetime import timedelta


def attendance_percentages(records):
    counts = {}
    for reg_no, day, status in records:
        counts.setdefault(reg_no, {"P": 0, "A": 0})
        counts[reg_no][status] += 1
    return {reg: value["P"] / (value["P"] + value["A"]) * 100
            for reg, value in counts.items()}


def three_day_absentees(records):
    by_student = {}
    for reg_no, day, status in records:
        by_student.setdefault(reg_no, []).append((day, status))
    result = []
    for reg_no, entries in by_student.items():
        entries.sort()
        streak, previous = 0, None
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
