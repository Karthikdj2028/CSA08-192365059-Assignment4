"""Process daily attendance CSV files and create monthly reports."""
import csv
from pathlib import Path


def process_month(input_folder, output_folder):
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)
    counts = {}
    errors = []

    if not input_folder.exists():
        raise FileNotFoundError(f"Input folder not found: {input_folder}")

    files = sorted(input_folder.glob("*.csv"))
    for filename in files:
        try:
            with open(filename, "r", encoding="utf-8", newline="") as file:
                reader = csv.reader(file)
                header = next(reader, None)
                if header != ["reg_no", "date", "status"]:
                    errors.append((filename.name, 1, "Wrong or missing header"))
                    continue

                for line_number, row in enumerate(reader, start=2):
                    if len(row) != 3:
                        errors.append((filename.name, line_number, "Expected 3 fields"))
                        continue
                    reg_no, day, status = [item.strip() for item in row]
                    status = status.upper()
                    if not reg_no or not day or status not in ("P", "A"):
                        errors.append((filename.name, line_number, "Invalid register, date or status"))
                        continue
                    counts.setdefault(reg_no, {"P": 0, "A": 0})
                    counts[reg_no][status] += 1
        except FileNotFoundError:
            errors.append((filename.name, 0, "File disappeared before reading"))
        except PermissionError:
            errors.append((filename.name, 0, "Permission denied"))
        except UnicodeDecodeError:
            errors.append((filename.name, 0, "File is not UTF-8"))

    summary = output_folder / "attendance_summary.csv"
    below = output_folder / "below_75.csv"
    error_log = output_folder / "errors.log"

    with open(summary, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["reg_no", "present", "absent", "percentage"])
        for reg_no, values in sorted(counts.items()):
            total = values["P"] + values["A"]
            percentage = values["P"] / total * 100 if total else 0
            writer.writerow([reg_no, values["P"], values["A"], f"{percentage:.2f}"])

    with open(below, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["reg_no", "attendance_percentage"])
        for reg_no, values in sorted(counts.items()):
            total = values["P"] + values["A"]
            percentage = values["P"] / total * 100 if total else 0
            if percentage < 75:
                writer.writerow([reg_no, f"{percentage:.2f}"])

    with open(error_log, "w", encoding="utf-8") as file:
        for filename, line_number, message in errors:
            file.write(f"{filename}, line {line_number}: {message}\n")

    return counts, errors


if __name__ == "__main__":
    base = Path(__file__).parent
    try:
        counts, errors = process_month(base / "input", base / "output")
        print("Students found:", len(counts))
        for reg_no, values in sorted(counts.items()):
            total = values["P"] + values["A"]
            pct = values["P"] / total * 100 if total else 0
            print(reg_no, "Present:", values["P"], "Absent:", values["A"],
                  "Attendance:", f"{pct:.2f}%")
        print("Damaged lines:", len(errors))
        print("Reports saved in Task02/output")
    except FileNotFoundError as error:
        print("Input error:", error)
