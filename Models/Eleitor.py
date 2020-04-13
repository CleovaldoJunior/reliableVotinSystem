from reliableVotinSystem.Models.Pessoa import Pessoa
from reliableVotinSystem.Models.Voto import Voto
from reliableVotinSystem.Banco import *

class Eleitor(Pessoa):
    def __init__(self, nome_p = None, idade_p = None, cpf_p = None, sexo_p = None, titulo_p = None):
        super().__init__(nome_p, idade_p, cpf_p, sexo_p)
        self.__titulo = titulo_p
        self.eleitorado = list()
        self.eleitorado_bd = list()
        self.recuperar_eleitorado()

    def set_titulo(self, titulo_p):
        self.__titulo = titulo_p

    def set_eleitorado_bd(self, eleitorado_p):
        self.eleitorado_bd = eleitorado_p

    def set_eleitorado(self, eleitores_p):
        self.__eleitores = eleitores_p

    def get_titulo(self):
        return self.__titulo

    def get_eleitorado(self):
        return self.eleitorado

    def get_eleitorado_bd(self):
        return self.eleitorado_bd

    def votar(self, n_candidato, tabulacao):
        voto = Voto(n_candidato)
        tabulacao.aplicar_voto(voto)

    def add_eleitor(self, eleitor):
        self.eleitorado.append(eleitor)

    def add_eleitor_bd(self, eleitor):
        inserir_eleitor_bd(eleitor)

    def remover_eleitor(self, eleitor):
        deletar_eleitor_bd(eleitor)

    def recuperar_eleitorado(self):
        eleitores = eleitores_bd()
        self.set_eleitorado_bd(eleitores)
