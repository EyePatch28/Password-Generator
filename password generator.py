import random
import string

def generate_password(length=12, uppercase=True, numbers=True, special_chars=True):
    """
    Generate a random password with the specified length and character types.
    
    Args:
        length (int): The length of the password (default is 12).
        uppercase (bool): Whether to include uppercase letters (default is True).
        numbers (bool): Whether to include numbers (default is True).
        special_chars (bool): Whether to include special characters (default is True).
    
    Returns:
        str: The generated password.
    """
    # Define the character set based on user preferences
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    # Generate the password by randomly choosing characters from the defined character set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """
    Main function to interact with the user and generate passwords.
    """
    print("Welcome to the Password Generator!")
    
    # Ask the user for input: number of passwords, password length, and character preferences
    num_passwords = int(input("How many passwords would you like to generate? "))
    password_length = int(input("Enter the length for each password: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    include_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    # Generate and print the specified number of passwords
    for _ in range(num_passwords):
        password = generate_password(
            length=password_length,
            uppercase=include_uppercase,
            numbers=include_numbers,
            special_chars=include_special_chars
        )
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
