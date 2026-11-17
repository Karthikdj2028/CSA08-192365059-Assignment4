"""Completed TODO exercise from Assignment 4, Task 3."""
import os
import tempfile


class InvalidRecord(Exception):
    """Raised when a line of the attendance file is not in the expected format."""


def parse_line(line):
    """'192311001,2026-10-08,P' -> ('192311001', '2026-10-08', 'P')"""
    parts = line.strip().split(",")
    if len(parts) != 3:
        raise InvalidRecord(f"expected 3 fields, found {len(parts)}")

    reg_no, day, status = parts
    if status not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{status}'")
    return reg_no, day, status


def summarise(path):
    present, absent, errors = 0, 0, []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                try:
                    reg_no, day, status = parse_line(line)
                except InvalidRecord as error:
                    errors.append((line_number, str(error)))
                else:
                    if status == "P":
                        present += 1
                    else:
                        absent += 1
    except FileNotFoundError as error:
        raise RuntimeError("attendance file was not found") from error
    except PermissionError as error:
        raise RuntimeError("permission denied while reading attendance file") from error
    else:
        return present, absent, errors
    finally:
        print("Finished reading attendance file.")


data = ("192311001,2026-10-08,P\n192311002,2026-10-08,A\n"
        "192311003,2026-10-08\n192311004,2026-10-08,L\n")
with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                 encoding="utf-8") as tmp:
    tmp.write(data)
    sample_path = tmp.name

try:
    print(summarise(sample_path))
finally:
    os.remove(sample_path)

try:
    summarise("attendance_file_that_does_not_exist.csv")
except RuntimeError as error:
    print("Handled:", error)
    print("Original cause:", type(error.__cause__).__name__)
