import random
import string

def generate_password(length, complexity):
    """Generates a random password based on desired length and complexity."""

    characters = string.ascii_letters
    if complexity == "A.High":
        characters += string.punctuation+string.digits
    elif complexity == "B.Medium":
        characters += string.digits

    password = "".join(random.choice(characters) for _ in range(length))
    return password
# Get user input
password_length = int(input("Enter the desired length of password: "))
print("Choose the level complexity:")
print("A.High")
print("B.Medium")
print("C.No")
complexity = input("Enter your choice (A, B, or C): ")
# Generate and print password
password = generate_password(password_length, complexity)
print("\nGenerated password:", password)