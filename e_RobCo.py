# Encryption file
import random
import string
import getch
import bcrypt
import os


def encrypt_user(i):
    return ''.join(
        random.choice(string.ascii_letters + string.digits + string.punctuation + string.hexdigits + string.octdigits)
        for _ in range(i)
    )


def encoded_input(message):
    print(message, end='')
    ei = ""
    while True:
        symbol = getch.getch()
        if symbol == "\n" or symbol == "\r":
            break
        print("*", end="", flush=True)
        ei += symbol
    print()
    return ei


# Password
def store_password(file_path, hashed_password):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        f.write(hashed_password)


def read_password(file_path):
    with open(file_path, 'rb') as f:
        return f.read()


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password)


def encrypt_password(plain_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode(), salt)
    return hashed_password
