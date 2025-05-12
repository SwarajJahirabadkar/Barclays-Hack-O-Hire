import string
import random
import hashlib
import bcrypt
from datetime import timedelta

# Common weak passwords dataset (RockYou-like)
COMMON_PASSWORDS = {"password", "123456", "qwerty", "letmein", "monkey", "football", "summer2024"}

# Analyze password strength
def analyze_password_strength(password):
    reasons = []
    strength = "Weak"

    # Check common passwords
    if password.lower() in COMMON_PASSWORDS:
        reasons.append("Password is commonly used.")

    # Check length
    if len(password) < 8:
        reasons.append("Too short, should be at least 8 characters.")
    elif len(password) > 32:
        reasons.append("Too long, maximum is 32 characters.")

    # Check variety of characters
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if not (has_upper and has_lower and has_digit and has_special):
        reasons.append("Should include uppercase, lowercase, digits, and special characters.")

    # If all conditions met, it's strong
    if len(password) >= 12 and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif len(password) >= 10:
        strength = "Moderate"

    return strength, reasons

# Estimate crack time using SHA-256 and bcrypt
def estimate_crack_time(password):
    # Simulate hash cracking time using hashing methods
    hash_sha256 = hashlib.sha256(password.encode()).hexdigest()
    hash_bcrypt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Example lookup table for crack time (simplified estimation)
    crack_times = {
        "Weak": "Seconds to minutes",
        "Moderate": "Hours to days",
        "Strong": "Years to centuries"
    }

    strength, _ = analyze_password_strength(password)
    return crack_times[strength]

# Suggest stronger alternatives
def suggest_secure_passwords(password):
    # Convert weak passwords into stronger alternatives
    transformations = {
        "o": "0", "i": "1", "a": "@", "s": "$", "e": "3",
        "l": "1", "t": "7", "b": "8", "g": "9"
    }
    
    new_passwords = []
    for _ in range(3):  # Generate 3 alternatives
        modified = "".join(transformations.get(c, c) for c in password)
        modified += random.choice(string.punctuation) + random.choice(string.ascii_letters)
        new_passwords.append(modified)

    return new_passwords

# Main function to generate and analyze password
def generate_and_analyze_password(password):
    # Analyze password strength
    strength, reasons = analyze_password_strength(password)
    
    # Estimate time to crack
    crack_time = estimate_crack_time(password)
    
    # Suggest more secure passwords if the strength is weak or moderate
    suggestions = []
    if strength != "Strong":
        suggestions = suggest_secure_passwords(password)

    return strength, reasons, suggestions, crack_time
