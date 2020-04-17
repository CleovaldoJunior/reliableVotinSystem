from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def gerarKeys_rsa():
   keyPair = RSA.generate(1024)
   pubKey = keyPair.publickey()
   return (pubKey, keyPair)

def encryption_rsa(plaintext, pub_key):
   plaintext= bytes(plaintext, 'utf-8')
   encryptor = PKCS1_OAEP.new(pub_key)
   encrypted = encryptor.encrypt(plaintext)
   return encrypted

def decrypt_rsa(ciphertext, priv_key):
   decryptor = PKCS1_OAEP.new(priv_key)
   decrypted = decryptor.decrypt(ciphertext)
   return decrypted.decode("utf-8")




