"""Read and validate registrations from one department CSV."""
import csv
from .validator import validate_row, InvalidRegistration


def read_department(filename):
    records = []
    errors = []
    try:
        with open(filename, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header != ["reg_no", "name", "department", "email", "events"]:
                errors.append((filename, 1, "wrong or missing header"))
                return records, errors

            for line_number, row in enumerate(reader, start=2):
                if not row:
                    continue
                try:
                    records.append(validate_row(row))
                except InvalidRegistration as error:
                    errors.append((filename, line_number, str(error)))
    except FileNotFoundError:
        errors.append((filename, 0, "department file is missing"))
    except PermissionError:
        errors.append((filename, 0, "permission denied"))
    except UnicodeDecodeError:
        errors.append((filename, 0, "file is not UTF-8"))
    return records, errors
