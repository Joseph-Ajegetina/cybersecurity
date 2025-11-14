import random

def generate_key():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = list(alphabet)
    random.shuffle(key)
    return "".join(key)

def encrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for char in text.upper():
        if char in alphabet:
            index = alphabet.find(char)
            result += key[index]
        else:
            result += char
    return result

def decrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for char in text.upper():
        if char in key:
            index = key.find(char)
            result += alphabet[index]
        else:
            result += char
    return result
