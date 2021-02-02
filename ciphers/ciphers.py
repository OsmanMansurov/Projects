import string

#the caesar cipher
def caesar_encrypt(plaintext, key):
    """plaintext, the text to encrypt. key, a key from 1 to 26"""
    result = ""
    for i in plaintext: #go through each element of the string
        if i.isupper(): #check if the string is uppercase or lowercase
            newChar = chr((ord(i) + key - 65) % 26 + 65) #perform the cipher
            result += newChar #append result onto the result string
        elif i.islower():
            newChar = chr((ord(i) + key - 97) % 26 + 97) #perform the cipher
            result += newChar #append result onto the result string
        else:
            result += i #if the character is not alphabetical, just add it
    return result #return result

def caesar_decrypt(ciphertext, key):
    """ciphertext, the text to decrypt. key, a key from 1 to 26"""
    result = ""
    for i in ciphertext: #subtracting key instead of adding
        if i.isupper():
            newChar = chr((ord(i) - key - 65) % 26 + 65)
            result += newChar
        elif i.islower():
            newChar = chr((ord(i) - key - 97) % 26 + 97)
            result += newChar
        else:
            result += i
    return result #return result

#the atbash cipher
def atbash(text):
    """text: enter in the plaintext to encrypt, ciphertext to decrypt"""
    result = ""
    #make the alphabets
    alphabetU, alphabetL = string.ascii_uppercase, string.ascii_lowercase
    reversedU = alphabetU[::-1]
    reversedL = alphabetL[::-1]
    for i in text: #perform the encryption
        if i.isupper():
            index = alphabetU.find(i)
            result += reversedU[index]
        elif i.islower():
            index = alphabetL.find(i)
            result += reversedL[index]
        else:
            result += i
    return result #return result

#the rail fence cipher
def railfence_encrypt(s,n):
    """s: the plaintext, n: the number of rails"""
    fence = [[] for i in range(n)]
    rail = 0
    var = 1

    for char in s:
        fence[rail].append(char)
        rail += var

        if rail == n-1 or rail == 0:
            var = -var
    res = ''
    for i in fence:
        for j in i:
            res += j
    return res

def railfence_decrypt(s,n):
    """s: the ciphertext, n: the number of rails"""
    fence = [[] for i in range(n)]
    rail  = 0
    var   = 1

    for char in s:
        fence[rail].append(char)
        rail += var

        if rail == n-1 or rail == 0:
            var = -var

    rFence = [[] for i in range(n)]

    i = 0
    l = len(s)
    s = list(s)
    for r in fence:
        for j in range(len(r)):
            rFence[i].append(s[0])
            s.remove(s[0])
        i += 1

    rail = 0
    var  = 1
    r = ''
    for i in range(l):
        r += rFence[rail][0]
        rFence[rail].remove(rFence[rail][0])
        rail += var

        if rail == n-1 or rail == 0:
            var = -var
    return r
#the affine cipher

def affine_encrypt(message, a, b):
    """message: the message to encrypt
       a: a number that MUST be coprime with 26
       b: an arbitrary number"""
    result = ""
    #convert the message to uppercase
    message = message.upper()
    #perform the normal affine cipher encryption
    for i in message:
        x = a * ord(i)
        newChar = chr((x + b - 65) % 26 + 65)
        result += newChar
    return result #return result

def affine_decrypt(message, a, b):
    """message: the message to decrypt
       a: a number that MUST be coprime with 26
       b: an arbitrary number"""
    result = ""
    #convert the message to uppercase
    message = message.upper()
    #perform the normal decryption
    for i in message:
        #find the multiplicative inverse of a
        for j in range(0, 26):
            if (a * j) % 26 == 1:
                modInverse = j
                break
        newChar = chr((modInverse * (ord(i) - b - 65)) % 26 + 65)
        result += newChar
    return result #return result

#the hill cipher (empty for now)
