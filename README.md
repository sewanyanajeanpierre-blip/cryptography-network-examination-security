# Cryptography and Network Security Assignment

This repository contains the completed project assignments for the Polytechnic Institute security review. It includes a risk assessment framework, a functional Python security toolkit, and firewall verification logs.

## Repository Contents
* `risk_assessment.md` - Section 1: Identification and ranking of assets, vulnerabilities, and controls.
* `security_toolkit.py` - Section 2: Core Python encryption, decryption, and SHA-256 integrity validation module.
* `filter_tests.md` - Section 3: Laboratory log containing firewall rules and implementation test results.
* `.gitignore` - Safeguards the system by preventing the local encryption key (`secret.key`) from being uploaded.

---

## Project Structure

```text
cryptography-network-security-exam/
├── .gitignore             # Excludes secret.key from version control
├── README.md              # Project documentation and execution instructions
├── filter_tests.md        # Section 3: Firewall rules and lab test logs
├── risk_assessment.md     # Section 1: Asset identification and risk matrix
└── security_toolkit.py    # Section 2: Python encryption and integrity script
```


## Installation & Environment Setup

To run the Python security toolkit locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd cryptography-network-security-exam
   ```

2. **Install dependencies:**
   This project utilizes the `cryptography` library for strong symmetric encryption. Install it using pip:
   ```bash
   pip install cryptography
   ```

---

## Execution Instructions

Run the automated Python security toolkit using the standard Python interpreter:

```bash
python security_toolkit.py
```

### Expected Behavior & Operations:
* **Key Generation:** If `secret.key` is missing, the script generates a cryptographic token locally and alerts you *not* to push it online.
* **File Encryption:** Automated encryption of sample records into a secure `.enc` format.
* **Integrity Validation:** Automatically calculates and matches SHA-256 cryptographic hashes before and after data handling to verify perfect document integrity.
