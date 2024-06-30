import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character set must be selected!!")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("RANDOM PASSWORD GENERATOR")
    
    length = int(input("Enter the desired length of the password: "))
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
