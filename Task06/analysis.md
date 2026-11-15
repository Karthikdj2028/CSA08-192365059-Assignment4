# Task 6 – College Fest Registration Desk

## Stage 1: requirements

Inputs are five department CSV files. Every valid row contains register number, student name, department, e-mail and a semicolon-separated event list. The program must tolerate missing files, invalid e-mails and damaged rows without stopping.

Outputs:
- clean_master.csv: one row for each unique register number;
- events/: one CSV participant list for every event;
- summary.txt: counts of unique students, valid rows and participants per event;
- errors.log: source filename, line number and reason.

Testable requirements: a repeated register number appears once in the master file; duplicate rows add new events and e-mails; a malformed row is logged; invalid e-mail is logged; a missing department file is logged; every valid event has an output CSV.

## Stage 2: processing flow

START → list the five expected department files → read each file → validate field count and e-mail → log invalid rows → check register number in dictionary → merge e-mails and events into sets → write master list → write event-wise lists → write summary and error log → END.

## Stage 3: design decisions

The register number is the identity key. A dictionary gives average O(1) lookup. Sets merge event and e-mail values and remove duplicates. E-mail checking uses simple string methods: it must contain @ and a dot after @. Invalid records are caught using InvalidRegistration. FileNotFoundError, PermissionError and UnicodeDecodeError are handled in the reader. The sample deliberately omits department5.csv to demonstrate a missing department file.

## Stage 4: package structure and pseudocode

Package:
- fest/validator.py: custom exception and row validation;
- fest/reader.py: file reading and error capture;
- fest/merge.py: dictionary and set-based merging;
- fest/report.py: master, event, summary and error outputs;
- run_fest.py: main program.

Pseudocode:

START
SET all_records TO empty list
SET all_errors TO empty list
FOR each expected department file
    READ file line by line
    IF file is missing THEN
        ADD missing-file message to all_errors
    ELSE
        FOR each data row
            VALIDATE the five fields
            IF row is invalid THEN
                ADD file name, line number and reason to all_errors
            ELSE
                ADD valid registration to all_records
            ENDIF
        ENDFOR
    ENDIF
ENDFOR
SET merged TO dictionary keyed by register number
FOR each valid registration
    ADD e-mail and events to sets for that register number
ENDFOR
WRITE clean master list
WRITE one participant file for each event
WRITE summary and error log
END

## Stage 5: demonstration

The sample files include a duplicate register number across two departments, one invalid e-mail, one damaged row and a missing fifth department file. Run the program and inspect Task06/output/.

## Alternative: compare each pair

A pairwise duplicate search compares each new record with earlier records and takes O(n²) comparisons for n registrations. A dictionary keyed by register number takes O(n) average total processing time. Both approaches need O(n) storage to keep the unique contact data; the dictionary additionally stores hash-table entries. The dictionary is selected because it scales better as registrations increase.

## Limitations

The design assumes register number identifies one student. If a student enters a wrong register number twice, those records will not merge. The e-mail check is intentionally simple and does not prove that an address exists.
