"""Main script imports the attendance utility module."""
from pathlib import Path
from attendance_utils import RECORDS, save_report

if __name__ == "__main__":
    output = Path(__file__).parent / "output" / "three_day_absent.txt"
    print("Three consecutive absence list:", save_report(RECORDS, output))
