# Task 3 – Exceptions in the attendance processor

## Failure table

| Failure | Exception or response |
|---|---|
| Folder or file missing | FileNotFoundError |
| No read permission | PermissionError |
| Invalid UTF-8 bytes | UnicodeDecodeError |
| Missing fields or invalid P/A status | Custom InvalidRecord |
| Text used where a number is expected | ValueError |
| Accessing a missing list position | IndexError |
| Empty file | No records; report zero present/absent |
| Wrong CSV header | Record a format error and continue |

## Custom exception
InvalidRecord is raised inside parse_line() when a line does not have exactly three fields or its status is not P/A. summarise() catches it for that line, records the line number and continues to the next line.

## Complete try statement
The processor uses try for file access, specific except blocks for file and encoding failures, an inner except for InvalidRecord, else to return a successful summary, and finally to print a completion message. raise RuntimeError(...) from error preserves the original exception as __cause__.

## Misuse experiment
misuse_demo.py deliberately uses a misspelled variable. A specific NameError handler prints the error. Replacing it with except Exception: pass hides the error and lets the program continue as if nothing happened. This can produce incomplete or incorrect attendance totals.

## Alternative: look before you leap
The alternative checks len(parts), status and required fields with if statements before using them. It still takes O(1) checks per line and O(n) for n lines. Raising and catching an exception has extra overhead only when a bad line occurs. If bad lines are rare, exception-based validation is clear and efficient. If bad lines are common, checking conditions first avoids creating exception objects repeatedly.
