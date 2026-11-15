"""Main script that connects the three modules."""
from pathlib import Path
from reader import RECORDS
from stats import three_day_absentees
from report import write_report

if __name__ == "__main__":
    result = three_day_absentees(RECORDS)
    output = Path(__file__).parent / "output" / "three_day_absent.txt"
    write_report(result, output)
    print("Three consecutive absence list:", result)
