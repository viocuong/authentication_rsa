from Crypto.PublicKey import RSA

keyPair = RSA.generate(bits=1024)
print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")
n = keyPair.n
e = keyPair.e
d = keyPair.d
msg = str(2039498524703445341710546041409128839646203009195).encode()

from hashlib import sha512
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
signature = pow(hash,d, n)
print("Signature:", hex(signature))
M = str(2039498524703445341710546041409128839646203009195)
msg = M.encode()

hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, e, n)
print("Signature valid:", hash == hashFromSignature)