"""College fest registration processing package."""
from .reader import read_department
from .merge import merge_registrations
from .report import write_outputs

__all__ = ["read_department", "merge_registrations", "write_outputs"]
