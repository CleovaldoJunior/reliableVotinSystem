from reliableVotinSystem.Security.RSA import *
class Voto:
    def __init__(self, id_candidato, public_key):
        self.__cipher_vote = encryption(id_candidato, public_key)

    def get_cipher_vote(self):
        return self.__cipher_vote

