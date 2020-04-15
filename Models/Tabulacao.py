from reliableVotinSystem.Security.RSA import *
class Tabulacao:

    def __init__(self):
        self.__votos = list()
        self.__keys = get_keys(256)

    # Autentica o voto na sessão atual
    def aplicar_voto(self, voto):
        cipher_text = voto.get_cipher_vote()
        self.get_votos().append(voto)

    # Retorna a lista de votos da sessão atual
    def get_votos(self):
        return self.__votos
