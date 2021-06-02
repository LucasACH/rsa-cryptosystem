import string
import sympy
from text import welcomeMessage, keysExplainMessage, startMessage, generateKeys1, showPandQ, showNandλ, showPublicAndSecret, encryptMessage1, encryptMessage2, encryptMessage3, encryptMessage4, decryptMessage1, decryptMessage2, goodByeMessage
from math import gcd
from progress.bar import ChargingBar

characters = [character for character in string.printable]

def convert(decryptedNumericMessage):
    message = "" 
    return (message.join(decryptedNumericMessage))


def main():
    print(welcomeMessage)
    input("[PRESS ENTER TO CONTINUE]")
    print(keysExplainMessage)
    input("[PRESS ENTER TO CONTINUE]")
    print(startMessage)
    input("[PRESS ENTER TO CONTINUE]")
    return generateKeys()


def generateKeys():
    print(generateKeys1)
    input("[PRESS ENTER TO GENERATE]")

    p = sympy.randprime(100,400)
    q = sympy.randprime(1000,2000)

    print(showPandQ(p, q))
    input("[PRESS ENTER TO CALCULATE]")
    
    n = p * q
    λ = (p - 1) * (q - 1)

    print(showNandλ(n, λ))
    input("[PRESS ENTER TO CALCULATE]")

    publicKey = sympy.randprime(0,λ - 1)
    secretKey = sympy.mod_inverse(publicKey,λ)

    print(showPublicAndSecret(publicKey, secretKey))
    input("[PRESS ENTER TO ENCRYPT]")

    return encryptMessage()


def encryptMessage():
    print(encryptMessage1)
    n = input("*     <//- N VALUE -//>  ----> ")
    publicKey = input("*     <//- PUBLIC KEY -//>  ----> ")

    print(encryptMessage2)
    message = input("*     ")
    print(" ")

    chargingBar = ChargingBar("Encrypting", max=len(message))

    numericMessage = []
    for char in message:
        numericMessage.append(characters.index(char))

    encryptedMessage = []
    for number in numericMessage:
        encryptedMessage.append((number**int(publicKey)) % int(n))
        chargingBar.next()

    encryptedMessage =  str(encryptedMessage).strip('][').replace(", ", "&")
    chargingBar.finish()
    
    print(encryptMessage3)
    input("[PRESS ENTER TO REVEAL]")

    print(" ")
    print(encryptedMessage)

    print(encryptMessage4)
    input("[PRESS ENTER TO DECRYPT]")

    return decryptMessage()


def decryptMessage():
    print(decryptMessage1)
    n = input("*     <//- N VALUE -//>  ----> ")
    secretKey = input("*     <//- SECRET KEY -//>  ----> ")

    print(decryptMessage2)
    message = input("*     ").strip('][').split('&')
    print(" ")

    numericMessage = [ int(number) for number in message ]
    chargingBar = ChargingBar("Decrypting", max=len(numericMessage))

    decryptedNumericMessage = []
    for number in list(message):
        decryptedNumericMessage.append((int(number)**int(secretKey)) % int(n))
        chargingBar.next()

    decryptedMessage = [characters[number] for number in decryptedNumericMessage]
    chargingBar.finish()

    print(" ")
    print("-- Output --->     " + convert(decryptedMessage))

    return goodBye()

def goodBye():
    print(goodByeMessage)
    return None



if __name__ == "__main__":
    main()