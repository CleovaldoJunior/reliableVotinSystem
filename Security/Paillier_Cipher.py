from phe import paillier

def generate_keys():
    ppk = paillier.PaillierPrivateKeyring()
    public_key, private_key = paillier.generate_paillier_keypair(ppk, 128)
    return (public_key,private_key)

public_key, private_key = generate_keys()

def encrypt(n_candidato):
    encrypted = public_key.encrypt(n_candidato)
    return encrypted

def decrypt(cipher):
    return private_key.decrypt(cipher)

def decrypt_list(cipher_list):
    cipher_add = cipher_list[0]
    for i in range(1,len(cipher_list)):
        cipher_add = cipher_add.__add__(cipher_list[i])
    return private_key.decrypt(cipher_add)