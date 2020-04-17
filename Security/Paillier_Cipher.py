from phe import paillier
def generate_keys():
    ppk = paillier.PaillierPrivateKeyring()
    public_key, private_key = paillier.generate_paillier_keypair(ppk, 128)
    return (public_key,private_key)

def encrypt(n_candidato, proof, public_key):
    encrypted = public_key.encrypt(n_candidato)
    return encrypted

kp = generate_keys()
new_kp = generate_keys()
votos = [(10**5,1),(10**3,1),(10**2,1),(10**3,1),(10**2,1),(10**3,1),(10**10,1)]
encrypted = [encrypt(x[0],x[1],kp[0]) for x in votos]
aux = encrypted[0]
for i in range(1,len(encrypted)):
    aux = aux.__add__(encrypted[i])
print(aux)
print(kp[1].decrypt(aux))

#[private_key.decrypt(x) for x in encrypted_number_list]