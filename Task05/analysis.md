# Task 5 – The Same Utility Organised Four Ways

All four versions read the same input file, input/attendance.csv. Each produces two outputs: attendance_summary.txt and three_day_absent.txt. A valid record has a register number, date and P/A status.

## (a) One script
single_script.py contains the file reading, percentage calculation, consecutive-absence calculation and report writing in one file.

## (b) One module imported by main
module_version/attendance_utils.py contains the reusable functions. module_version/main.py imports and calls them.

## (c) Three modules in one folder
three_modules/reader.py reads records, stats.py calculates results, report.py writes the outputs, and main.py connects them.

## (d) Package
package_version/attendance/ is a Python package. __init__.py exposes the reading, statistics and reporting functions. Each responsibility has its own sub-module.

## Change effort for adding the second report

| Organisation | Files changed | Explanation |
|---|---:|---|
| One script | 1 | The second calculation and report are added in the same file. |
| One utility module + main | 2 | Add the calculation/report function in the module and call it from main. |
| Three modules | 3 | Update stats.py, report.py and main.py. |
| Package | 3 | Update attendance/stats.py, attendance/report.py and package main.py. |

The table counts source files that need code changes for this example. File creation can increase the count when a new report file is required.

## Comparison

| Organisation | Readability | Reuse | Testing | Naming conflicts |
|---|---|---|---|---|
| One script | Simple for a small task; becomes long | Low | Functions are mixed with the entry point | More likely |
| One module | Main program is separate from functions | Good | The utility can be imported and tested | Low |
| Three modules | Each responsibility is clear | Very good | Reader, stats and report tested separately | Low with clear names |
| Package | Suitable for a larger application | Very good | Small package modules independently tested | Low when imports are explicit |

## Import statements

- import attendance.stats imports the module path. Call attendance.stats.three_day_absentees().
- from attendance import stats imports the stats sub-module through the package. Call stats.three_day_absentees().
- from attendance.stats import three_day_absentees imports the function directly.

## Alternative: keep everything in one script

A single script avoids package-loading overhead and is suitable for a very small program. A package has a one-time import cost: Python executes each module when it is first imported and caches it in sys.modules. Later imports reuse the loaded module. The extra memory is the module objects and code; it is small compared with the attendance data. A package makes it easier to locate a function and change one responsibility without searching through a long script.
