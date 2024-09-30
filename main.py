import re

def password_strength(password):
    # Initialize score and message
    score = 0
    feedback = []

    # Check the length of the password
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short, should be at least 8 characters.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters for better strength.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters for better strength.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include numbers to strengthen your password.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters (e.g., @, #, $, etc.).")

    # Determine strength based on score
    if score == 5:
        return "Strong password!", feedback
    elif score >= 3:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

# Example Usage
password = input("Enter a password to check its strength: ")
strength, tips = password_strength(password)

print(f"Password strength: {strength}")
if tips:
    print("Suggestions for improvement:")
    for tip in tips:
        print(f"- {tip}")