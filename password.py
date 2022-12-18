import random

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!§$%&/()=?+*#.^"

def generate_password(length):
    string = LOWER + UPPER + NUMBERS + SYMBOLS
    password = "".join(random.sample(string, length))
    print('Password: ' + password)

generate_password(16)
