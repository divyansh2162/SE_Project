# Reflection — Lab 5: Static Code Analysis

**Important:** The uploaded three-page handout refers to four reflection questions, but it does not include their actual wording. The responses below are a concise reflection draft based on the lab's stated learning outcomes. If your instructor provided a separate page with the four exact questions, use that wording instead.

### 1. What is static code analysis, and why is it useful?
Static code analysis checks source code without running the program. It helps identify likely bugs, unsafe coding patterns, unused code, and style problems early. This makes code easier to maintain and reduces the chance of issues reaching users.

### 2. What did Pylint, Bandit, and Flake8 help identify?
Pylint is useful for general code quality and maintainability, such as naming, unused arguments, and module structure. Bandit focuses on security patterns, including shell command execution and hard-coded credentials. Flake8 checks PEP 8 formatting and common style violations.

### 3. Which issues were most important, and how were they fixed?
The highest-risk findings were the shell command built using string concatenation and the hard-coded password-like value. The unused shell helper and credential were removed because the demonstration did not need them. The mutable default argument was changed to `None`, the unused currency argument was removed, and naming/formatting were cleaned up.

### 4. How did you verify that the changes did not affect the program?
I ran the original and corrected scripts using the same sample meter readings. Both completed successfully and produced identical console output and bill totals. The final static-analysis verification still needs to be run locally with Pylint, Bandit, and Flake8; their genuine reports should be saved as the before/after evidence.
