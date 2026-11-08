#!/bin/bash
set -euo pipefail

python -m pylint electricity_bill_original.py > pylint_report_before.txt || true
python -m bandit -r electricity_bill_original.py > bandit_report_before.txt || true
python -m flake8 electricity_bill_original.py > flake8_report_before.txt || true

python -m pylint electricity_bill.py > pylint_report_after.txt || true
python -m bandit -r electricity_bill.py > bandit_report_after.txt || true
python -m flake8 electricity_bill.py > flake8_report_after.txt || true

echo "Reports generated. Check the final Pylint score and review Bandit/Flake8 output."
