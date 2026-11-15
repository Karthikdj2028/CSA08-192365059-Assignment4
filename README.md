# CSA08-192365059-Assignment4

**Assignment:** Robust Data Processing with Files, Exceptions, Modules and Packages (CO4)  
**Student:** Karthikeyan S  
**Register Number:** 192365059  
**Platform:** Windows 10  
**Python:** 3.11.6 (`python`)  
**Libraries:** Python standard library only; no third-party packages required.

Repository: https://github.com/Karthikdj2028/CSA08-192365059-Assignment4

## Tasks and run commands

Run commands from this repository's root folder in the VS Code terminal.

| Folder | Assignment task | Main command | Result |
|---|---|---|---|
| Task01 | File-processing design review | `python Task01/repair_mess.py` | Reads mess bills line by line, totals decimal amounts, and reports rejected lines. |
| Task02 | Biometric attendance files | `python Task02/attendance_processor.py` | Processes all daily CSV files and creates monthly percentage and below-75% reports plus an error log. |
| Task03 | Exception handling | `python Task03/exceptions_attendance.py` | Demonstrates InvalidRecord, line-number errors, try/except/else/finally and missing-file handling. |
| Task04 | File and exception forensics | `python Task04/file_forensics.py` | Reproduces overwrite/no-newline defects, then demonstrates append mode and error logging. |
| Task05 | Four code organisations | See commands below | Compares one script, one module, three modules and a package; each creates a three-consecutive-absence report. |
| Task06 | College Fest Registration Desk | `python Task06/run_fest.py` | Validates and merges department registrations and writes master, event, summary and error files. |

### Task05 commands

```powershell
python Task05/single_script.py
python Task05/module_version/main.py
python Task05/three_modules/main.py
python Task05/package_version/main.py
```

## Files and outputs

Each task contains source code, a short analysis/complexity explanation, sample input data where applicable, and an `evidence/` folder. Run the programs to create their output files. Screenshots in the evidence folders must be captured by the student from their own Windows execution; the placeholder README files are not screenshots.

Task02 writes `attendance_summary.csv`, `below_75.csv` and `errors.log` under `Task02/output/`. Task06 writes the clean master list, event-wise participant files, summary and error log under `Task06/output/`.

## GitHub workflow

Commit each task separately after running it and saving its screenshot. Example:

```powershell
git add Task01
git commit -m "feat(task01): repair hostel mess bill processor"
git push origin main
```

Do the same for Task02 through Task06. Do not use a single final commit for the whole assignment.

## Limitations and assumptions

- Sample attendance data is provided for demonstration; replace or add daily CSVs for a full month.
- Attendance percentage is present records divided by valid P/A records for each student.
- Fest duplicate registrations are detected by normalised register number; the first valid registration is retained.
- E-mail validation is a simple introductory string check, not full RFC validation.
