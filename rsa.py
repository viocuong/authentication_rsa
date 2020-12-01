from Crypto.PublicKey import RSA
keyPair = RSA.generate(bits=2048)
print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

msg = 1234567
from hashlib import sha512
signature = pow(msg, keyPair.d, keyPair.n)
print("Signature:", hex(signature))

msg = 1234567
#hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print(hashFromSignature)