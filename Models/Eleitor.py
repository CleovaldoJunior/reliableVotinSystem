from reliableVotinSystem.Models.Pessoa import Pessoa
from reliableVotinSystem.Models.Voto import Voto

class Eleitor(Pessoa):

    def __init__(self, nome_p, idade_p, cpf_p, sexo_p, titulo_p):
        super().__init__(nome_p, idade_p, cpf_p, sexo_p)
        self.__titulo = titulo_p

    def set_titulo(self, titulo_p):
        self.__titulo = titulo_p

    def get_titulo(self):
        return self.__titulo

    def votar(self, n_candidato, tabulacao):
        voto = Voto(n_candidato)
        tabulacao.aplicar_voto(voto)
