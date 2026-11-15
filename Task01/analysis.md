# Task 1 – File-processing design review

## 1.1 Defects in the original script

| Defect | Possible hostel-office problem |
|---|---|
| Hard-coded Windows path | The program fails on another computer or when the file moves. |
| File is not closed | The operating system may keep the file handle open, especially after an error. |
| f.read() loads the full file | A large 50,000-line file consumes memory for the complete text plus split lines. |
| Bare except with pass | Permission, format and programming errors are silently hidden. |
| int(amount) is used | An amount such as 1250.50 raises ValueError and paise cannot be represented. |
| Repeated string concatenation | Rebuilding a long report repeatedly creates unnecessary string objects. |
| Empty final line | Splitting on newline creates an empty record which can fail during indexing. |
| Rejected rows are not recorded | The clerk cannot correct or audit a student bill that was skipped. |

## 1.2 Repaired design

The program takes the filename as a parameter, uses with open(), reads one line at a time, parses amounts with Decimal, catches only expected data errors, and returns a list of rejected lines with their line numbers.

## 1.3 Design defence (under 100 words)

The repaired program is safer for 50,000 lines because it does not create one giant string and a second list of all lines. The with statement closes the file even if processing fails. Decimal preserves paise exactly. Specific checks prevent one damaged row from stopping the remaining records, while the rejected-line list gives the hostel office an audit trail. A parameterised filename also allows the same function to process a new month's file without editing the source code.

## Alternative: read() or readlines()

Both approaches still take O(n) time to inspect n characters or lines. read() stores the whole text string; readlines() stores a list of all line strings, so both need O(file size) extra memory. Iterating over the file reads one line at a time, so the input-reading buffer is approximately O(one line). The report and rejected-line lists still require memory for the results.

## Complexity

For n lines, processing is O(n) time. Memory for reading is O(one line); report and rejected records take O(r + e), where r is accepted rows and e is rejected rows.
