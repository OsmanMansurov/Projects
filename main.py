import string

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

def atbash(plaintext):
    result = ""
    alphabetU, alphabetL = string.ascii_uppercase, string.ascii_lowercase
    reversedU = alphabetU[::-1]
    reversedL = alphabetL[::-1]
    for i in plaintext:
        if i.isupper():
            index = alphabetU.find(i)
            result += reversedU[index]
        elif i.islower():
            index = alphabetL.find(i)
            result += reversedL[index]
        else:
            result += i
    return result
