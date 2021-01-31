import random

#cipher storage

def caesar_encrypt(plaintext, key):
    result = ""
    for i in plaintext:
        if i.isupper():
            newChar = chr((ord(i) + key - 65) % 26 + 65)
            result += newChar
        elif i.islower():
            newChar = chr((ord(i) + key - 97) % 26 + 97)
            result += newChar
        else:
            result += i
    return result

def caesar_decrypt(plaintext, key):
    result = ""
    for i in plaintext:
        if i.isupper():
            newChar = chr((ord(i) - key - 65) % 26 + 65)
            result += newChar
        elif i.islower():
            newChar = chr((ord(i) - key - 97) % 26 + 97)
            result += newChar
        else:
            result += i
    return result
