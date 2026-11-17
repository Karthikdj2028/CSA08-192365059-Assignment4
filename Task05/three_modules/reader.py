"""Reader module: read valid P/A records from a CSV file."""
import csv
from datetime import date


def read_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            if row["status"] in ("P", "A"):
                records.append((row["reg_no"], date.fromisoformat(row["date"]), row["status"]))
    return records
