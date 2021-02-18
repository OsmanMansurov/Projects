def encrypt(plaintext, a, b):
    result = ""
    alphabetU = "QWERTYUIOPASDFGHJKLZXCVBNM"
    alphabetL = alphabetU.lower()
    for i in plaintext:
        if i.isalpha():
            if i.isupper():
                x = a * alphabetU.find(i)
                newChar = alphabetU[(x + b) % 26]
                result += newChar
            elif i.islower():
                x = a * alphabetL.find(i)
                newChar = alphabetL[(x + b) % 26]
                result += newChar
        elif i == ".":
            result += ","
        elif i == "?":
            result += "$"
        elif i == "!":
            result += "#"
        elif i == "'":
            result += "."
        else:
            result += i
    return result

def decrypt(ciphertext, a, b):
    result = ""
    alphabetU = "QWERTYUIOPASDFGHJKLZXCVBNM"
    alphabetL = alphabetU.lower()
    for i in ciphertext:
        if i.isalpha():
            for j in range(0, 26):
                if (a * j) % 26 == 1:
                    modInverse = j
                    break
            if i.isupper():
                index = alphabetU.find(i)
                newChar = alphabetU[(modInverse * (index - b)) % 26]
                result += newChar
            elif i.islower():
                index = alphabetL.find(i)
                newChar = alphabetL[(modInverse * (index - b)) % 26]
                result += newChar
        elif i == ",":
            result += "."
        elif i == "$":
            result += "?"
        elif i == "#":
            result += "!"
        elif i == ".":
            result += "'"
        else:
            result += i
    return result

