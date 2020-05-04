# Resolve the problem!!
import string
import random

LOWER_LETTERS = list('abcdefghijklmnopqrstuvwxyz')
UPPER_LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
DIGITS = list('0123456789')
SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here
    password = random.choice(LOWER_LETTERS + UPPER_LETTERS + DIGITS + SYMBOLS)
    
    create_secure_password = []
    for i in range(3, 16):
        for j in range(2):
            select = random.randint(0, len(LOWER_LETTERS) -1)
            choose = LOWER_LETTERS[select]
            password = random.choice
        j=0

        for j in range(2):
            select = random.randint(0, len(UPPER_LETTERS) -1)
            choose = UPPER_LETTERS[select]
            password = random.choice
        j=0
        
        for j in range(2):
            select = random.randint(0, len(DIGITS) -1)
            choose = DIGITS[select]
            password = random.choice
        j=0

        for j in range(2):
            select = random.randint(0, len(SYMBOLS) -1)
            choose = SYMBOLS[select]
            password = random.choice
        j=0

    return create_secure_password


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
