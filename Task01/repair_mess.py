"""Repair a hostel mess-bill file processor using safe file handling."""
from decimal import Decimal, InvalidOperation
from pathlib import Path


def process_mess_file(filename):
    """Return report lines, total amount and rejected-line details."""
    report = []
    rejected = []
    total = Decimal("0.00")

    # The file is read one line at a time and closed automatically.
    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if line.strip() == "":
                continue

            parts = [item.strip() for item in line.strip().split(",")]
            if len(parts) != 3:
                rejected.append((line_number, line.strip(), "Expected 3 fields"))
                continue

            reg_no, name, amount_text = parts
            try:
                amount = Decimal(amount_text)
            except InvalidOperation:
                rejected.append((line_number, line.strip(), "Amount is not numeric"))
                continue

            if amount < 0:
                rejected.append((line_number, line.strip(), "Amount cannot be negative"))
                continue

            report.append(f"{reg_no} {name} Rs {amount:.2f}")
            total += amount

    return report, total, rejected


if __name__ == "__main__":
    filename = Path(__file__).parent / "mess_oct.txt"
    try:
        lines, total, rejected = process_mess_file(filename)
        print("MESS BILL REPORT")
        for line in lines:
            print(line)
        print("TOTAL: Rs", format(total, ".2f"))

        print("\nREJECTED LINES")
        for item in rejected:
            print(item)
    except FileNotFoundError:
        print("Input file not found:", filename)
    except PermissionError:
        print("Permission denied while reading:", filename)
