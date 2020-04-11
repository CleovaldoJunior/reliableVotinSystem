from reliableVotinSystem.Models.Eleitor import Eleitor

class Candidato(Eleitor):

    def __init__(self, nome_p, idade_p, cpf_p, sexo_p, titulo_p, n_candidato_p):
        super().__init__(nome_p, idade_p, cpf_p, sexo_p, titulo_p)
        self.__n_candidato = n_candidato_p

    def set_n_candidato(self, n_candidato_p):
        self.__n_candidato = n_candidato_p

    def get_n_candidato(self):
        return self.__n_candidato