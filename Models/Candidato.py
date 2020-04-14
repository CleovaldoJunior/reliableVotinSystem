from reliableVotinSystem.Models.Eleitor import Eleitor
from reliableVotinSystem.Banco import *

class Candidato(Eleitor):

    def __init__(self, nome_p=None, idade_p=None, cpf_p=None, sexo_p=None, titulo_p=None, id_candidato_p=None):
        super().__init__(nome_p, idade_p, cpf_p, sexo_p, titulo_p)
        self.__id_candidato = id_candidato_p
        self.__candidatos = list()
        self.__candidatos_bd = list()
        self.recuperar_candidatos()

    def set_id_candidato(self, n_candidato_p):
        self.__n_candidato = n_candidato_p

    def set_candidatos(self, candidatos_p):
        self.__candidatos = candidatos_p

    def set_candidatos_bd(self, candidatos_bd_p):
        self.__candidatos_bd = candidatos_bd_p

    def get_id_candidato(self):
        return self.__id_candidato

    def get_candidatos(self):
        return self.__candidatos

    def get_candidatos_bd(self):
        return self.__candidatos_bd

    def add_candidato(self, candidato):
        self.__candidatos.append(candidato)

    def add_candidato_bd(self, candidato):
        inserir_candidato_bd(candidato)

    def deletar_candidato_id(self, id_candidato):
        index = 0
        for candidato in self.get_candidatos():
            if candidato.get_id_candidato() == id_candidato:
                self.get_candidatos().pop(index)
            index+=1

    def remover_candidato(self, id_candidato):
        self.deletar_candidato_id(id_candidato)
        deletar_candidato_bd(id_candidato)

    def recuperar_candidatos(self):
        candidatos = candidatos_bd()
        self.set_candidatos_bd(candidatos)