"""Write attendance reports."""
from pathlib import Path


def write_report(reg_numbers, filename):
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(reg_numbers) + ("\n" if reg_numbers else ""), encoding="utf-8")
    return path
