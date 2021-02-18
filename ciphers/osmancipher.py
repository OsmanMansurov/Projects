def main():
    while True:
        inp = input("Would you like to encrypt, or decrypt? e/d: ")
        if inp == "e":
            plaintext = input("Plaintext: ")
            a = int(input("Key A (must be coprime with 27): "))
            b = int(input("Key B: "))
            ciphertext = encrypt(plaintext, a, b)
            print(f"Ciphertext: {ciphertext}")
        elif inp == "d":
            ciphertext = input("Ciphertext: ")
            a = int(input("Key A (must be coprime with 27): "))
            b = int(input("Key B: "))
            plaintext = decrypt(ciphertext, a, b)
            print(f"Plaintext: {plaintext}")
        else:
            print("Invalid input")
        inp2 = input("Do you wish to exit? y/n: ")
        if inp2 == "y" or inp2 == "Y":
            break
        elif inp2 == "n" or inp2 == "N":
            continue
        else:
            print("Confused. Continuing loop.")


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

if __name__ == "__main__":
    main()
