"""Simple validation for one college fest registration row."""


class InvalidRegistration(Exception):
    """Raised for a damaged or invalid registration row."""


def validate_row(row):
    if len(row) != 5:
        raise InvalidRegistration(f"expected 5 fields, found {len(row)}")

    reg_no, name, department, email, events_text = [item.strip() for item in row]
    if not reg_no or not name or not department:
        raise InvalidRegistration("register number, name and department are required")

    email_lower = email.lower()
    if "@" not in email_lower or "." not in email_lower.split("@")[-1]:
        raise InvalidRegistration("invalid email address")

    events = [event.strip() for event in events_text.split(";") if event.strip()]
    if not events:
        raise InvalidRegistration("at least one event is required")

    return {
        "reg_no": reg_no,
        "name": name,
        "department": department,
        "email": email_lower,
        "events": events
    }
