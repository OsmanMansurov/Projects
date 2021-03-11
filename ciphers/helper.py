import ciphers
import time
import osmancipher

def main():
    while True:
        inp1 = input("Welcome to the cipher helper. Would you like to encrypt (e) text, or decrypt (d) text? ")
        if inp1 == "e" or inp1 == "E":
            inp2 = input("What cipher would you like to use? Caesar, Atbash, RailFence, Affine, OMC, or quit: ")
            if inp2 == "Caesar":
                plaintext = input("Plaintext: ")
                key = int(input("Key: "))
                print(ciphers.caesar_encrypt(plaintext, key))
            elif inp2 == "Atbash":
                plaintext = input("Plaintext: ")
                print(ciphers.atbash(plaintext))
            elif inp2 == "RailFence":
                plaintext = input("Plaintext: ")
                key = int(input("Key: "))
                print(ciphers.railfence_encrypt(plaintext, key))
            elif inp2 == "Affine":
                plaintext = input("Plaintext: ")
                a = int(input("Key a (must be coprime with 27): "))
                b = int(input("Key b: "))
                print(ciphers.affine_encrypt(plaintext, a, b))
            elif inp2 == "OMC":
                plaintext = input("Plaintext: ")
                a = int(input("Key a (must be coprime with 27): "))
                b = int(input("Key b: "))
                print(osmancipher.encrypt(plaintext, a, b))
            elif inp2 == "quit" or inp2 == "Quit":
                break
            else:
                print("Sorry, I did not understand you're input")
        elif inp1 == "d" or inp1 == "D":
            inp2 = input("What cipher would you like to use? Caesar, Atbash, RailFence, Affine, OMC, or quit ")
            if inp2 == "Caesar":
                ciphertext = input("Ciphertext: ")
                key = int(input("Key: "))
                print(ciphers.caesar_decrypt(ciphertext, key))
            elif inp2 == "Atbash":
                ciphertext = input("Ciphertext: ")
                print(ciphers.atbash(ciphertext))
            elif inp2 == "RailFence":
                ciphertext = input("Ciphertext: ")
                key = int(input("Key: "))
                print(ciphers.railfence_decrypt(ciphertext, key))
            elif inp2 == "Affine":
                ciphertext = input("Ciphertext: ")
                a = int(input("Key a (must be coprime with 27): "))
                b = int(input("Key b: "))
                print(ciphers.affine_decrypt(ciphertext, a, b))
            elif inp2 == "OMC":
                ciphertext = input("Ciphertext: ")
                a = int(input("Key a (must be coprime with 27): "))
                b = int(input("Key b: "))
                print(osmancipher.decrypt(ciphertext, a, b))
            elif inp2 == "quit" or inp2 == "Quit":
                break
            else:
                print("Sorry, I did not understand you're input")
        else:
            print("I did not understand your input, please try again")
            time.sleep(1)
            continue



if __name__ == "__main__":
    main()
