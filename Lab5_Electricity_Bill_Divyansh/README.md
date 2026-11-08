# Lab 5 — Static Code Analysis: Electricity Bill Calculator

Assigned repository: https://github.com/SETAPESU26/L5_30_electricity_bill

## Files
- `electricity_bill.py` — corrected version.
- `electricity_bill_original.py` — baseline copy for comparison.
- `issues.md` — findings table and fixes.
- `reflection.md` — reflection draft (the supplied handout does not show the four question wordings).
- `run_analysis.sh` — creates before/after reports using the required tools.
- `pylint_report_before.txt`, `bandit_report_before.txt`, `flake8_report_before.txt` — placeholders: run the script locally to replace them with actual tool output.
- `pylint_report_after.txt`, `bandit_report_after.txt`, `flake8_report_after.txt` — placeholders: run the script locally to replace them with actual tool output.

## Run on macOS
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pylint bandit flake8

# Baseline reports
python -m pylint electricity_bill_original.py > pylint_report_before.txt || true
python -m bandit -r electricity_bill_original.py > bandit_report_before.txt || true
python -m flake8 electricity_bill_original.py > flake8_report_before.txt || true

# Corrected reports
python -m pylint electricity_bill.py > pylint_report_after.txt || true
python -m bandit -r electricity_bill.py > bandit_report_after.txt || true
python -m flake8 electricity_bill.py > flake8_report_after.txt || true

# Run the demonstration and compare with the original output
python electricity_bill_original.py
python electricity_bill.py
```

Do not submit the placeholder report files as completed evidence. Replace them with the output generated on your machine. Confirm that the final Pylint score is above 9.5 and that Bandit/Flake8 findings are resolved.

## Suggested three-commit sequence
After copying the corrected file and documentation into your fork:
1. `git add electricity_bill_original.py issues.md && git commit -m "Document baseline static analysis findings"`
2. `git add electricity_bill.py && git commit -m "Fix security and code quality issues"`
3. `git add *_report_*.txt reflection.md run_analysis.sh README.md && git commit -m "Add static analysis verification and lab reflection"`

The third commit should be made only after replacing report placeholders with real reports. Push your branch with `git push`.
