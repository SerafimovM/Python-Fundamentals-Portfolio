import re
from typing import List, Dict

"""
SECURITY VALIDATOR
Author: Martin Serafimov
Description: Input validation using Regular Expressions (Regex) and conditional logic.
"""

def validate_email(email: str) -> bool:
    """
    Validates if the provided string is a valid email format using Regex.
    Pattern checks for: characters @ domain . extension
    """
    if not isinstance(email, str) or not email.strip():
        raise ValueError("Email must be a non-empty string")
    
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def extract_phone_numbers(text: str) -> List[str]:
    """
    Extracts all phone numbers matching format XXX-XXX-XXXX from text.
    Returns a list of found phone numbers.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    pattern = r"\d{3}-\d{3}-\d{4}"
    return re.findall(pattern, text)

def check_password_complexity(password: str) -> Dict[str, bool | str]:
    """
    Analyzes password strength based on multiple criteria.
    Returns a dictionary with individual checks and overall score.
    """
    if not isinstance(password, str) or not password:
        raise ValueError("Password must be a non-empty string")
    
    results = {
        "length": len(password) >= 8,
        "has_upper": bool(re.search(r"[A-Z]", password)),
        "has_digit": bool(re.search(r"\d", password)),
        "has_special": bool(re.search(r"[!@#$%^&*]", password))
    }
    
    score = sum(results.values())
    results["score"] = f"{score}/4"
    return results

def censor_sensitive_data(text: str) -> str:
    """
    Replaces credit card numbers (16 digits) with [REDACTED] for security.
    Supports formats: XXXX-XXXX-XXXX-XXXX or XXXX XXXX XXXX XXXX
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    return re.sub(pattern, "[REDACTED]", text)

if __name__ == "__main__":
    test_email = "martin.serafimov@example.com"
    print(f"Is '{test_email}' valid? {validate_email(test_email)}")
    
    raw_text = "Call me at 555-123-4567 or the office at 555-987-6543."
    print(f"Found numbers: {extract_phone_numbers(raw_text)}")
    
    pw = "SuperSecret1!"
    print(f"Password Analysis for '{pw}': {check_password_complexity(pw)}")
    
    log_entry = "User payment processed with card 1234-5678-1234-5678 successfully."
    print(f"Log: {censor_sensitive_data(log_entry)}")