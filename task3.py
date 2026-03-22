import string

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase check
    if any(char.isupper() for char in password):
        score += 1

    # Lowercase check
    if any(char.islower() for char in password):
        score += 1

    # Digit check
    if any(char.isdigit() for char in password):
        score += 1

    # Special character check
    if any(char in string.punctuation for char in password):
        score += 1

    # Strength result
    if score <= 2:
        return "Weak Password"
    elif score <= 4:
        return "Medium Password"
    else:
        return "Strong Password"


# Main Program
print("Password Strength Checker")

password = input("Enter your password: ")
strength = check_password_strength(password)

print("Password Strength:", strength)