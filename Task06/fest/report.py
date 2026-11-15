"""Write clean master list, event lists, summary and error log."""
import csv
from pathlib import Path


def write_outputs(merged, errors, output_folder):
    output = Path(output_folder)
    event_folder = output / "events"
    event_folder.mkdir(parents=True, exist_ok=True)

    master_path = output / "clean_master.csv"
    with open(master_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["reg_no", "name", "department", "emails", "events"])
        for reg_no in sorted(merged):
            item = merged[reg_no]
            writer.writerow([
                item["reg_no"], item["name"], item["department"],
                ";".join(sorted(item["emails"])),
                ";".join(sorted(item["events"]))
            ])

    event_people = {}
    for item in merged.values():
        for event in item["events"]:
            event_people.setdefault(event, []).append(item["reg_no"])

    for event, reg_numbers in event_people.items():
        safe_name = "".join(ch.lower() if ch.isalnum() else "_" for ch in event)
        with open(event_folder / f"{safe_name}.csv", "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["reg_no"])
            for reg_no in sorted(set(reg_numbers)):
                writer.writerow([reg_no])

    with open(output / "summary.txt", "w", encoding="utf-8") as file:
        file.write(f"Unique students: {len(merged)}\n")
        valid_rows = sum(item["row_count"] for item in merged.values())
        file.write(f"Valid registration rows: {valid_rows}\n")
        file.write(f"Events: {len(event_people)}\n")
        for event in sorted(event_people):
            file.write(f"{event}: {len(set(event_people[event]))} participants\n")

    with open(output / "errors.log", "w", encoding="utf-8") as file:
        for filename, line_number, message in errors:
            file.write(f"{filename}, line {line_number}: {message}\n")

    return master_path
