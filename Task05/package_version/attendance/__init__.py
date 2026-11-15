"""Attendance processing package."""
from .stats import three_day_absentees
from .report import write_report

__all__ = ["three_day_absentees", "write_report"]
