import random
import string

def generate_password(length, upper=True, lower=True, numbers=True, symbols=True):
    characters = ""

    if upper:
        characters += string.ascii_uppercase

    if lower:
        characters += string.ascii_lowercase

    if numbers:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if characters == "":
        return "Please select at least one character type."

    password = []

    if upper:
        password.append(random.choice(string.ascii_uppercase))

    if lower:
        password.append(random.choice(string.ascii_lowercase))

    if numbers:
        password.append(random.choice(string.digits))

    if symbols:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password[:length])


print("=" * 45)
print("        SECURE PASSWORD GENERATOR")
print("=" * 45)

try:
    length = int(input("Enter password length (Minimum 4): "))

    if length < 4:
        print("Password length must be at least 4.")
    else:
        print("\nInclude the following?")
        upper = input("Uppercase Letters (Y/N): ").lower() == "y"
        lower = input("Lowercase Letters (Y/N): ").lower() == "y"
        numbers = input("Numbers (Y/N): ").lower() == "y"
        symbols = input("Special Characters (Y/N): ").lower() == "y"

        if not (upper or lower or numbers or symbols):
            print("\nPlease select at least one character type.")
        else:
            password = generate_password(length, upper, lower, numbers, symbols)

            print("\n" + "=" * 45)
            print("Generated Password:")
            print(password)
            print("=" * 45)

except ValueError:
    print("Please enter a valid number.")