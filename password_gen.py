import string
import random

def generate_password(password_length):
    # Define the sets.
    alphabets = list(string.ascii_letters)
    numbers = list(string.digits)
    special_characters = list(string.punctuation)

    # Ensure at least one character from each category.
    password = [
        random.choice(alphabets),
        random.choice(numbers),
        random.choice(special_characters),
    ]

    # Combine all categories for random selection.
    all_char = alphabets + numbers + special_characters

    # Fill in the rest of characters.
    password += random.choices(all_char,k=password_length-3)

    # Shuffle the characters.
    random.shuffle(password)
    
    # Convert the list into string.
    return ''.join(password)

def main():
    # Ask the user for desired password length.
    while True:
        try:
            length = int(input("Enter a desired length of the password (minimum 3): "))
            # Since at least one character from each category must be there.
            if length < 3:
                print("Enter a value greater than 3")
            else:
                break
        except ValueError:
            print("Please enter a number")
    
    # Generate and print the password.
    print("Generated Password:", generate_password(length))

main()