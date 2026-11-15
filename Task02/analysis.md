# Task 2 – Biometric attendance files

## Data model
Each daily CSV has reg_no, date and status columns. Register number and date are text; status is P or A. A dictionary keyed by register number stores present and absent counters. The program creates attendance_summary.csv, below_75.csv and errors.log.

## File operations
Use pathlib to list the daily CSV files. Open inputs in r mode with UTF-8 and newline="", then process with csv.reader iteration. Open reports in w mode because they are regenerated each run. Use write() for the error log. The with statement closes each file.

## Pseudocode
START
INPUT folder containing daily attendance CSV files
SET counts TO empty dictionary
SET errors TO empty list
FOR each CSV file in folder
    OPEN file for reading
    FOR each line with its line number
        IF line does not contain exactly three fields THEN
            ADD file name, line number and error to errors
        ELSE
            CHECK register number, date and P/A status
            IF record is valid THEN
                INCREASE the student's present or absent count
            ELSE
                ADD file name, line number and reason to errors
            ENDIF
        ENDIF
    ENDFOR
    CLOSE file
ENDFOR
WRITE attendance summary
WRITE below-75-percent report
WRITE error log
END

## Trace
day01.csv line 2 adds one present for 192311001. Line 3 adds one absent for 192311002. Line 5 has invalid status X and line 6 has only two fields; both are logged. day02.csv adds the remaining valid records.

## Alternative and complexity
Rereading all files for every student takes O(s*f*l) time for s students, f files and l lines per file. Reading each file once and updating a dictionary takes O(f*l). The dictionary needs O(s) counter space; rereading can use O(1) extra memory but repeats I/O.
