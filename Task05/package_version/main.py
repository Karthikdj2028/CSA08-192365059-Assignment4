"""Main program that uses the attendance package."""
from pathlib import Path
from attendance import reader, three_day_absentees, write_report

if __name__ == "__main__":
    results = three_day_absentees(reader.RECORDS)
    output = Path(__file__).parent / "output" / "three_day_absent.txt"
    write_report(results, output)
    print("Three consecutive absence list:", results)
    print("Report saved:", output)
