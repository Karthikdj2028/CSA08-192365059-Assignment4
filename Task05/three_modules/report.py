"""Report module: write attendance summary and consecutive-absence report."""
from pathlib import Path


def write_reports(percentages, absentees, output_folder):
    output = Path(output_folder)
    output.mkdir(parents=True, exist_ok=True)
    with open(output / "attendance_summary.txt", "w", encoding="utf-8") as file:
        for reg_no, value in sorted(percentages.items()):
            file.write(f"{reg_no}: {value:.2f}%\n")
    with open(output / "three_day_absent.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(sorted(absentees)))
