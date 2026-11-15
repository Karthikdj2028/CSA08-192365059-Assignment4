"""Run the college fest registration desk package."""
from pathlib import Path
from fest.reader import read_department
from fest.merge import merge_registrations
from fest.report import write_outputs


def main():
    base = Path(__file__).parent
    input_folder = base / "input"
    output_folder = base / "output"
    department_files = [
        "department1.csv", "department2.csv", "department3.csv",
        "department4.csv", "department5.csv"
    ]

    all_records = []
    all_errors = []

    for name in department_files:
        records, errors = read_department(input_folder / name)
        all_records.extend(records)
        all_errors.extend(errors)

    merged = merge_registrations(all_records)
    master = write_outputs(merged, all_errors, output_folder)

    print("Valid rows:", len(all_records))
    print("Unique students:", len(merged))
    print("Rejected or missing-file entries:", len(all_errors))
    print("Master list:", master)
    print("Event lists, summary and errors saved in output/")


if __name__ == "__main__":
    main()
