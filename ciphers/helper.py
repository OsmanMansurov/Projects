import ciphers
import time

def main():
    while True:
        inp1 = input("Welcome to the cipher helper. Would you like to encrypt (e) text, or decrypt (d) text? ")
        if inp1 == "e" or inp1 == "E":
            pass
        elif inp1 == "d" or inp1 == "D":
            pass
        else:
            print("I did not understand your input, please try again")
            time.sleep(1)
            continue



if __name__ == "__main__":
    main()
