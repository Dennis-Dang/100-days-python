# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
NUM_LETTERS = random.randint(8, 10)
NUM_SYMBOLS = random.randint(2, 4)
NUM_NUMBERS = random.randint(2, 4)


def generate_password():
    password_list = []
    # Generate letters
    password_letters = [random.choice(letters) for _ in range(NUM_LETTERS)]

    # Generate numbers
    password_numbers = [random.choice(numbers) for _ in range(NUM_NUMBERS)]

    # Generate symbols
    password_symbols = [random.choice(symbols) for _ in range(NUM_SYMBOLS)]

    # Combine letters, numbers, and symbols together
    password_list += password_letters+password_numbers+password_symbols

    # Randomize order of characters in password
    random.shuffle(password_list)

    return ''.join(password_list)
