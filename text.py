welcomeMessage = """
+___________________________________________________________________________+
|                                                                           |
|    Welcome! RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem      |
|    that is widely used for secure data transmission. It is also one       |
|    of the oldest.                                                         |
|                                                                           |
|    I made a simple DEMO for further understanding. Lets beginn!           |                
+___________________________________________________________________________+
"""

keysExplainMessage = """
+___________________________________________________________________________+
|                                                                           |
|    The keys for the RSA algorithm are generated in the following way:     |
|                                                                           |
|    (1) Choose two distinct prime numbers p and q.                         |
|        (p and q are kept secret)                                          |
|                                                                           |
|    (2) Compute n = pq. (n is released as part of the public key)          |
|                                                                           |
|    (3) Compute λ(n), where λ is Carmichael's totient function.            |
|        (λ(n) is kept secret)                                              |
|                                                                           |
|    (4) Choose an integer e such that 1 < e < λ(n) and gcd(e,λ(n)) = 1;    |
|        that is, e and λ(n) are coprime.                                   |
|        (e is released as part of the public key)                          |
|                                                                           |
|    (5) Determine d as d ≡ e−1 (mod λ(n)); that is, d is the modular       |
|        multiplicative inverse of e modulo λ(n).                           |
|        (d is kept secret as the private key exponent)                     |
+___________________________________________________________________________+
"""

startMessage = """
+___________________________________________________________________________+
|                                                                           |
|     Let´s go strait into maths!                                           |
+___________________________________________________________________________+
"""

generateKeys1 = """
+___________________________________________________________________________+
|                                                                           |
|     p and q are generated randomly. They should be similar in magnitude   |
|     but differ in length by a few digits to make factoring harder.        |
+___________________________________________________________________________+
"""

def showPandQ(p, q):
    return """
+___________________________________________________________________________+
|                                                                           |
|     p = %s                                                               |
|     q = %s                                                              |
+___________________________________________________________________________+
|                                                                           |
|     Great! We can now calculate "n" and λ(n).                             |
+___________________________________________________________________________+ 
    """ % (p, q)

def showNandλ(n, λ):
    return """
+___________________________________________________________________________+
|                                                                           |
|     n = (p * q) = %s                                                  | 
|     λ(n) = (p - 1) * (q - 1) = %s                                     |
+___________________________________________________________________________+
|                                                                           |
|     Remember, "n" is released as part of the public key and λ(n)          |
|     is kept secret. The only thing left is to calculate the public key    |
|     and the secret key.                                                   |
+___________________________________________________________________________+
    """ % (n, λ)

def showPublicAndSecret(publicKey, secretKey):
    return """
+___________________________________________________________________________+
|                                                                           |
|     PUBLIC KEY = (Random prime between 0 and (λ - 1)) = %s            |
|     SECRET KEY = (Multiplicative inverse x of PK modulo λ(n)) = %s    |
+___________________________________________________________________________+
|                                                                           |
|     Cool! Let´s encrypt a message.                                        |
+___________________________________________________________________________+
    """ % (publicKey, secretKey)

encryptMessage1 = """
+___________________________________________________________________________+
|                                                                           |
|     We will need "n" and our public key to encrypt a message. Just        |
|     copy and paste them into the console.                                 |
+___________________________________________________________________________+
"""

encryptMessage2 = """
+___________________________________________________________________________+
|                                                                           |
|    Now write the message you want to encrypt.                             |
+___________________________________________________________________________+
"""

encryptMessage3 = """
+___________________________________________________________________________+
|                                                                           |
|    Great! Let´s see how it looks encrypted.                               |
+___________________________________________________________________________+
"""

encryptMessage4 = """
+___________________________________________________________________________+
|                                                                           |
|    Awesome! We can now try to decrypt it. With "n" and the secret key     |
|    should be enough.                                                      |
+___________________________________________________________________________+
"""

decryptMessage1 = """
+___________________________________________________________________________+
|                                                                           |
|     We will need "n" and our secret key to decrypt a message. Just        |
|     copy and paste them into the console.                                 |
+___________________________________________________________________________+
"""

decryptMessage2 = """
+___________________________________________________________________________+
|                                                                           |
|    Paste the message you want to decrypt.                                 |
+___________________________________________________________________________+
"""

goodByeMessage = """
+___________________________________________________________________________+
|                                                                           |
|    Good work! You just encrypted and decrypted your first message using   |
|    the RSA cryptosystem. Check the source code for details or visit       |
|    https://en.wikipedia.org/wiki/RSA_(cryptosystem) for further           |
|    information.                                                           |
|                                                                           |
|    ( ͡~ ͜ʖ ͡°) Made by Lucas Achaval                                      |     
+___________________________________________________________________________+
"""