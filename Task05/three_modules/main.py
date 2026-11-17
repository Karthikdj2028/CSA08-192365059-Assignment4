"""Main module joins reading, statistics and reporting."""
from pathlib import Path
from reader import read_records
from stats import attendance_percentages, three_day_absentees
from report import write_reports

if __name__ == "__main__":
    base = Path(__file__).parent
    records = read_records(base.parent / "input" / "attendance.csv")
    percentages = attendance_percentages(records)
    absentees = three_day_absentees(records)
    write_reports(percentages, absentees, base.parent / "output")
    print("Attendance percentages:", percentages)
    print("Absent for three consecutive days:", absentees)
