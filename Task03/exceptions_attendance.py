"""Custom exception and specific handling for attendance records."""
import os
import tempfile


class InvalidRecord(Exception):
    """Raised when an attendance line is not in the expected format."""


def parse_line(line):
    """Return register number, date and status after validation."""
    parts = line.strip().split(",")
    if len(parts) != 3:
        raise InvalidRecord(f"expected 3 fields, found {len(parts)}")
    reg_no, day, status = parts
    if status not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{status}'")
    if not reg_no or not day:
        raise InvalidRecord("register number and date cannot be blank")
    return reg_no, day, status


def summarise(path):
    present, absent, errors = 0, 0, []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                try:
                    record = parse_line(line)
                except InvalidRecord as error:
                    errors.append((line_number, str(error)))
                    continue
                else:
                    if record[2] == "P":
                        present += 1
                    else:
                        absent += 1
    except FileNotFoundError as error:
        raise RuntimeError("attendance file was not found") from error
    except PermissionError as error:
        raise RuntimeError("permission denied for attendance file") from error
    except UnicodeDecodeError as error:
        raise RuntimeError("attendance file is not UTF-8") from error
    else:
        return present, absent, errors
    finally:
        print("Finished checking:", path)


if __name__ == "__main__":
    data = (
        "192311001,2026-10-08,P\n"
        "192311002,2026-10-08,A\n"
        "192311003,2026-10-08\n"
        "192311004,2026-10-08,L\n"
    )
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                     encoding="utf-8") as tmp:
        tmp.write(data)
        sample_name = tmp.name

    try:
        print(summarise(sample_name))
        try:
            summarise("file_that_does_not_exist.csv")
        except RuntimeError as error:
            print("Handled:", error)
            print("Original cause:", type(error.__cause__).__name__)
    finally:
        os.remove(sample_name)
