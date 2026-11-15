# Task 5 – The same utility organised four ways

## The four organisations
(a) single_script.py keeps the sample rows, calculation and output in one file.  
(b) module_version/main.py imports attendance_utils.py; reusable functions are separated from the entry point.  
(c) three_modules separates sample data (reader.py), calculation (stats.py) and output (report.py). main.py connects them.  
(d) package_version uses an attendance package with __init__.py, reader.py, stats.py and report.py.

All versions identify a student with three consecutive calendar-day absences and write a second report called three_day_absent.txt. Each version uses if __name__ == "__main__" in its executable entry point.

## Change effort for the new report

| Organisation | Files changed for the added report | Reason |
|---|---:|---|
| One script | 1 | Add calculation and output in the same script. |
| One module + main | 2 | Add the function in the utility module and call it from main. |
| Three modules | 2 | Add the function to stats and the output function/call in report/main. |
| Package | 2 | Add the calculation in stats and output in report; package imports are already exposed. |

The exact count depends on the original separation and whether a new report file is created. These counts describe this example.

## Comparison

| Organisation | Readability | Reuse | Testing | Naming conflicts |
|---|---|---|---|---|
| One script | Easiest for a tiny task; grows crowded | Low | Functions can be tested but are mixed with main code | More likely |
| One module | Clear separation of main and reusable functions | Good | Utility can be imported and tested | Low |
| Three modules | Each responsibility is easy to locate | Very good | Reader, stats and report can be tested separately | Low with clear names |
| Package | Best for a growing attendance application | Very good | Small package modules are independently testable | Lowest when imports are explicit |

## Import forms

- import attendance.stats imports the module path; use attendance.stats.three_day_absentees().
- from attendance import stats imports the stats submodule through the package; use stats.three_day_absentees().
- from attendance.stats import three_day_absentees imports the function directly.

## Alternative: keep everything in one script

A single script avoids module-loading work and is adequate for a very small program. A package has a one-time import cost: Python executes each module the first time it is imported and keeps it in sys.modules. Later imports reuse the loaded module. The extra memory is the code and module objects, usually small compared with attendance data. For larger work, finding and changing a focused function is easier in a package.
