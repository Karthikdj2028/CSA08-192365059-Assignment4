"""Reproduce log overwrite and missing-newline defects, then repair them."""
from pathlib import Path

BASE = Path(__file__).parent
DATA = BASE / "input"
OUTPUT = BASE / "output"
DATA.mkdir(exist_ok=True)
OUTPUT.mkdir(exist_ok=True)


def save_returns_broken(books):
    # Defect: mode w truncates earlier days; no newline joins book names.
    log = open(OUTPUT / "broken_returns.log", "w", encoding="utf-8")
    for book in books:
        log.write(book)
    log.close()


def process_broken(day_file):
    try:
        books = (DATA / day_file).read_text(encoding="utf-8").split("\n")
        save_returns_broken([book for book in books if book])
    except FileNotFoundError:
        print("missing")


def save_returns_fixed(books):
    # Append mode preserves earlier days; newline separates each book.
    with open(OUTPUT / "returns.log", "a", encoding="utf-8") as log:
        for book in books:
            log.write(book + "\n")


def process_fixed(day_file):
    try:
        with open(DATA / day_file, "r", encoding="utf-8") as source:
            books = [line.strip() for line in source if line.strip()]
        save_returns_fixed(books)
    except FileNotFoundError as error:
        with open(OUTPUT / "errors.log", "a", encoding="utf-8") as log:
            log.write(f"{day_file}: {error}\n")
        print("Logged missing file:", day_file)


if __name__ == "__main__":
    (DATA / "day1.txt").write_text("The Alchemist\nAtomic Habits\n", encoding="utf-8")
    (DATA / "day2.txt").write_text("Python Basics\nClean Code\n", encoding="utf-8")
    (DATA / "day3.txt").write_text("Data Science\n", encoding="utf-8")

    for day in ("day1.txt", "day2.txt", "day3.txt"):
        process_broken(day)
    print("BROKEN LOG (only last day, joined lines):")
    print((OUTPUT / "broken_returns.log").read_text(encoding="utf-8"))

    (OUTPUT / "returns.log").write_text("", encoding="utf-8")
    (OUTPUT / "errors.log").write_text("", encoding="utf-8")
    for day in ("day1.txt", "day2.txt", "day3.txt", "missing_day.txt"):
        process_fixed(day)

    print("\nREPAIRED APPEND LOG:")
    print((OUTPUT / "returns.log").read_text(encoding="utf-8"))
    print("Error log:")
    print((OUTPUT / "errors.log").read_text(encoding="utf-8"))
