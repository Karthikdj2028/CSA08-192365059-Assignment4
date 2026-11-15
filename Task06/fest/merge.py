"""Merge duplicate registrations using a dictionary and sets."""


def merge_registrations(records):
    merged = {}
    for record in records:
        reg_no = record["reg_no"]
        if reg_no not in merged:
            merged[reg_no] = {
                "reg_no": reg_no,
                "name": record["name"],
                "department": record["department"],
                "emails": set(),
                "events": set(),
                "sources": set(),
                "row_count": 0
            }

        merged[reg_no]["emails"].add(record["email"])
        merged[reg_no]["events"].update(record["events"])
        merged[reg_no]["sources"].add(record["department"])
        merged[reg_no]["row_count"] += 1

    return merged
