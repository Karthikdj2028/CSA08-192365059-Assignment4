# Task 4 – File and exception forensics

## Defects
1. Opening returns.log with mode w truncates the existing log each day, so only the last day remains.
2. write(b) does not add a newline, so several book names become one long line.
3. If write() fails before close(), the manually opened file may remain open until cleanup by the runtime. A with statement closes it reliably.

## Evidence construction
file_forensics.py creates three day files, runs the broken function for each, and prints the resulting broken log. It then clears a separate repaired log, appends all three days, and attempts one missing file to demonstrate error logging.

## Repair
Use with open(..., "a", encoding="utf-8") for the week-long log and append a newline after each book. Use with open() for source files. Catch FileNotFoundError and write the error to errors.log rather than silently ignoring it.

## Prevention rules
- Always use with open() so files close even if an exception occurs.
- Select file mode deliberately: w replaces a file; a appends to it. Add explicit newline separators for record-based text logs.

## Alternative: try/finally
Manual handling can use file = open(...); try: write(...); finally: file.close(). The time and space complexities do not change: processing n book names is O(n) time and O(1) extra space when writing one at a time. With closes automatically even if an exception occurs. With manual close omitted in one error branch, a file handle can remain open; a correct finally block closes it.
