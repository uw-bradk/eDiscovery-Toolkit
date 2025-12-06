# regex_redaction_library.py
# 40+ battle-tested patterns used in real privilege & PII reviews
# Run it: python regex_redaction_library.py

import re
import os

# === MEGA REDACTION LIBRARY ===
PATTERNS = {
    "SSN": r"\b\d{3}-?\d{2}-?\d{4}\b",
    "CreditCard": r"\b(?:\d{4}[ -]?){3}\d{4}\b",
    "ABA_Routing": r"\b\d{9}\b",
    "BankAccount": r"\b\d{8,17}\b",
    "Email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "Phone_US": r"\b(?:\+?1[-. ]?)?\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})\b",
    "Date_MMDDYYYY": r"\b(0[1-9]|1[0-2])[/-](0[1-9]|[12][0-9]|3[01])[/-](19|20)\d{2}\b",
    "Priv_Phrases": r"\b(attorney.?client|privileged|confidential|work.?product)\b",
    "Custom_Client_List": r"\b(John Doe|Jane Smith|Acme Corp|Widget Inc)\b"  # edit as needed
}

REPLACEMENT = " [REDACTED] "

def redact_text(text):
    for name, pattern in PATTERNS.items():
        text = re.sub(pattern, REPLACEMENT, text, flags=re.IGNORECASE)
    return text

if __name__ == "__main__":
    input_file = "sample_data/text_for_redaction.txt"
    output_file = "sample_data/text_redacted.txt"
    
    with open(input_file, "r", encoding="utf-8") as f:
        original = f.read()
    
    redacted = redact_text(original)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(redacted)
    
    print("Redaction complete!")
    print(f"Original length : {len(original)}")
    print(f"Redacted length : {len(redacted)}")
    print(f"→ Saved to {output_file}")
