# Static Analysis Findings — Electricity Bill Calculator

The line numbers below refer to the original `electricity_bill.py` in the assigned repository.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Shell command execution with user-controlled input | Security (Bandit B605 / command injection risk) | 56–58 | `os.system()` builds a shell command by concatenating `meterIp`; a crafted value could alter the command. The helper also uses plain HTTP. | Removed the unused shell-based helper and its `os` import. If meter synchronisation is required later, implement it with a validated HTTP client, strict host allow-list, timeout, and HTTPS. |
| Hard-coded password-like value | Security (Bandit B105) | 12 | `CLERK_PASSWORD` embeds a password-like string directly in source and is not used by the demo. | Removed the unused credential. Real credentials must come from a protected environment/secret store, not source code. |
| Mutable default argument | Bug / maintainability | 38 | `extras={}` is shared between calls and can retain mutations unexpectedly. | Changed the default to `None` and create a fresh empty dictionary inside the function. |
| Unused function argument | Code quality (Pylint) | 46, 69 | `currency` is accepted by `averageBill()` but never used. | Removed the unnecessary parameter and updated the call site. |
| Non-PEP 8 naming | Style (Pylint / Flake8) | 15, 20, 26, 38, 46, 51, 56 | Function and parameter names use camelCase instead of `snake_case`. | Renamed functions and local variables to PEP 8 `snake_case`. |
| Missing main guard | Maintainability / testability (Pylint) | 75 | The demo runs whenever the module is imported, making reuse and testing harder. | Added `if __name__ == "__main__": main()`. |
| File opened without explicit encoding | Code quality (Pylint) | 52 | JSON output file is opened without specifying an encoding. | Added `encoding="utf-8"` to the file open call. |
| Unused import / unused constant | Code quality (Pylint) | 2, 12 | `os` and the hard-coded password constant were not needed by the actual billing demonstration. | Removed both after removing the unsafe unused helper. |
| Spacing and formatting violations | Style (Flake8) | 40, 70 and surrounding lines | Inconsistent spacing around dictionary keys and assignment operators, plus formatting that makes the code harder to scan. | Applied consistent spacing, wrapped long statements, and formatted the file using standard Python style. |

## Verification note

The baseline and corrected program were both executed locally. Their console output was identical, including the warning for the backwards M3 reading and the four calculated bills. Pylint, Bandit, and Flake8 were **not executable in the file-generation environment** because the tools were not installed and package installation could not reach PyPI. Run the supplied `run_analysis.sh` on your Mac to create genuine before/after reports and verify the Pylint target (>9.5); do not treat a predicted score as a measured score.
