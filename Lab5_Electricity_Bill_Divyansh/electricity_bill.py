"""Calculate demonstration electricity bills from meter readings."""

import json
from defusedxml import ElementTree as ET

SLABS = [(100, 3.5), (200, 5.0), (300, 6.5)]
HIGH_RATE = 8.0
FIXED_CHARGE = 75
TAX_RATE = 0.05
METER_XML = (
    "<meters>"
    "<meter id='M1' prev='1200' curr='1350'/>"
    "<meter id='M2' prev='5000' curr='5420'/>"
    "<meter id='M3' prev='800' curr='760'/>"
    "</meters>"
)


def read_meters(xml_text):
    """Return meter IDs and previous/current readings from XML."""
    root = ET.fromstring(xml_text)
    return [
        (meter.get("id"), int(meter.get("prev")), int(meter.get("curr")))
        for meter in root.findall("meter")
    ]


def calculate_units(previous, current):
    """Calculate consumed units; treat a backwards reading as zero usage."""
    if current < previous:
        print("Warning: meter reading went backwards")
        return 0
    return current - previous


def energy_charge(units):
    """Calculate energy charges using the configured tariff slabs."""
    charge = 0.0
    lower_limit = 0
    remaining_units = units

    for upper_limit, rate in SLABS:
        slab_units = min(remaining_units, upper_limit - lower_limit)
        if slab_units > 0:
            charge += slab_units * rate
            remaining_units -= slab_units
        lower_limit = upper_limit

    return charge + remaining_units * HIGH_RATE


def generate_bill(meter_id, units, tax_rate=TAX_RATE, extras=None):
    """Generate one bill without retaining mutable defaults between calls."""
    extra_charges = extras if extras is not None else {}
    amount = energy_charge(units) + FIXED_CHARGE + sum(extra_charges.values())
    bill = {
        "meter": meter_id,
        "units": units,
        "amount": round(amount * (1 + tax_rate), 2),
    }
    return bill


def average_bill(bill_records):
    """Return the average amount for a collection of bills."""
    if not bill_records:
        return 0.0
    total_amount = sum(bill["amount"] for bill in bill_records)
    return round(total_amount / len(bill_records), 2)


def save_bills(bill_records, file_name="bills.json"):
    """Save generated bills as formatted JSON."""
    with open(file_name, "w", encoding="utf-8") as bill_file:
        json.dump(bill_records, bill_file, indent=2)


def main():
    """Run the sample billing demonstration."""
    bill_records = []

    for meter_id, previous, current in read_meters(METER_XML):
        units = calculate_units(previous, current)
        bill_records.append(generate_bill(meter_id, units))

    bill_records.append(generate_bill("M4", 50, extras={"late_fee": 25}))

    for bill in bill_records:
        print(
            bill["meter"],
            "used",
            bill["units"],
            "units, bill Rs.",
            bill["amount"],
        )

    highest_bill = max(bill_records, key=lambda bill: bill["amount"])
    print("Highest bill:", highest_bill["meter"])
    print("Average bill:", average_bill(bill_records))

    total_billed = sum(bill["amount"] for bill in bill_records)
    print("Total billed:", round(total_billed, 2))

    save_bills(bill_records)
    print("Saved", len(bill_records), "bills to bills.json")


if __name__ == "__main__":
    main()
