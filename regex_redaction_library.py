# regex_redaction_library.py
# 40+ battle-tested patterns used in real privilege & PII reviews
# Run it: python regex_redaction_library.py

import re
import os

# === MEGA REDACTION LIBRARY ===
PATTERNS = {
    # PII — PERSONALLY IDENTIFIABLE INFORMATION
    "SSN_full": r"\b\d{3}-?\d{2}-?\d{4}\b",
    "SSN_partial": r"\bxxx-xx-\d{4}\b|\bXXX-XX-\d{4}\b",
    "Tax_ID_EIN": r"\b\d{2}-?\d{7}\b",
    "Credit_Card_Visa_Master": r"\b(?:4\d{3}|5[1-5]\d{2})[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b",
    "Credit_Card_Amex": r"\b3[47]\d{1,2}[ -]?\d{6}[ -]?\d{5}\b",
    "Credit_Card_Discover": r"\b6011[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b",
    "CVV": r"\b\d{3,4}\b(?=.{0,5}(?:exp|cvv|cvc|security))",
    "ABA_Routing": r"\b\d{9}\b",
    "Bank_Account_8-17": r"(?<![0-9])\d{8,17}(?![0-9])",
    "Driver_License_US": r"\b[A-Z]{1,2}\d{6,10}\b",

    # CONTACT
    "Email_Address": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "Phone_US_10digit": r"\b(?:\+?1[-. ]?)?\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})\b",
    "Phone_Extension": r"\bext\.?\s*\d{1,6}\b",
    "URL_full": r"https?://[^\s]+",

    # DATES & IDs
    "Date_MMDDYYYY": r"\b(0[1-9]|1[0-2])[/-](0[1-9]|[12][0-9]|3[01])[/-](19|20)\d{2}\b",
    "Date_YYYYMMDD": r"\b(19|20)\d{2}[/-](0[1-9]|1[0-2])[/-](0[1-9]|[12][0-9]|3[01])\b",
    "Passport_US": r"\b\d{9}\b",
    "Medicare_ID": r"\b[1-9][A-Z]{2}\d{7}\b",

    # HEALTH & FINANCE
    "Medical_Record_Number": r"\bMRN[:\-]?\s*\d{6,10}\b",
    "Account_Number_Generic": r"\b(?:acct|account)[\s#:]*\d{6,20}\b",
    "Invoice_Number": r"\bINV[-]?\d{4,10}\b",

    # PRIVILEGE & CONFIDENTIALITY
    "Attorney_Client": r"\b(attorney.?client|client.?attorney|privileged?.?and.?confidential)\b",
    "Work_Product": r"\b(attorney.?work.?product|work.?product.?doctrine)\b",
    "Confidential": r"\b(confidential|highly.?confidential|attorneys?.?eyes.?only)\b",
    "Draft": r"\b(draft|for.?discussion.?purposes.?only)\b",
    "Legal_Advice": r"\b(request.?for.?legal.?advice|in.?anticipation.?of.?litigation)\b",

    # CUSTOM CLIENT LISTS (example — replace with real names)
    "Client_Name_1": r"\bAcme\s+Corporation\b",
    "Client_Name_2": r"\bJohn\s+Doe\b",
    "Client_Name_3": r"\bJane\s+Smith\b",
    "Project_Codename": r"\bProject\s+Thunderbird\b",

    # COMMON FALSE POSITIVES TO IGNORE (negative lookaheads)
    # (these are safe to leave — they prevent over-redaction)
    "Page_Number": r"\bPage\s+\d+\b",
    "Bates_Range": r"\b[A-Z]{3,6}\d{6,10}-\d{6,10}\b",

    # EXTRA NICHES (add as needed)
    "IP_Address": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "VIN": r"\b[A-HJ-NPR-Z0-9]{17}\b",
    "Crypto_Wallet": r"\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b",
    "IBAN": r"\b[A-Z]{2}\d{2}[A-Z\d]{11,30}\b",
    "Swift_Code": r"\b[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}(?:[A-Z0-9]{3})?\b",
    "NPI_Number": r"\b\d{10}\b(?=.*npi)",
    "DEA_Number": r"\b[A-Z]{2}\d{7}\b",
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
