import rsa

def get_keys(bits):
   (pubkey, privkey) = rsa.newkeys(bits)
   return pubkey, privkey

def encryption(plaintext, public_key):
   plaintext = plaintext.encode('utf8')
   cipher = rsa.encrypt(plaintext, public_key)
   return cipher

def decrypt(cipher, private_key):
   plaintext = rsa.decrypt(cipher, private_key)
   return plaintext.decode('utf8')

