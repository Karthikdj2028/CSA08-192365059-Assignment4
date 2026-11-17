"""Attendance package public functions."""
from .reader import read_records
from .stats import attendance_percentages, three_day_absentees
from .report import write_reports

__all__ = ["read_records", "attendance_percentages", "three_day_absentees", "write_reports"]
