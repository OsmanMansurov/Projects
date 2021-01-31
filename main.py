import string

#cipher storage

def caesar_encrypt(plaintext, key):
    """plaintext, the text to encrypt. key, a key from 1 to 26"""
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

def caesar_decrypt(ciphertext, key):
    """ciphertext, the text to decrypt. key, a key from 1 to 26"""
    result = ""
    for i in ciphertext:
        if i.isupper():
            newChar = chr((ord(i) - key - 65) % 26 + 65)
            result += newChar
        elif i.islower():
            newChar = chr((ord(i) - key - 97) % 26 + 97)
            result += newChar
        else:
            result += i
    return result

def atbash(text):
    """plaintext: enter in the plaintext to encrypt, ciphertext to decrypt"""
    result = ""
    alphabetU, alphabetL = string.ascii_uppercase, string.ascii_lowercase
    reversedU = alphabetU[::-1]
    reversedL = alphabetL[::-1]
    for i in text:
        if i.isupper():
            index = alphabetU.find(i)
            result += reversedU[index]
        elif i.islower():
            index = alphabetL.find(i)
            result += reversedL[index]
        else:
            result += i
    return result
