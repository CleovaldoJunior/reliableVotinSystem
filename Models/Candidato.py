from reliableVotinSystem.Models.Eleitor import Eleitor
from reliableVotinSystem.Banco import *


class Candidato(Eleitor):

    def __init__(self, nome_p=None, idade_p=None, cpf_p=None, sexo_p=None, titulo_p=None, id_candidato_p=None, n_candidato = None):
        super().__init__(nome_p, idade_p, cpf_p, sexo_p, titulo_p)
        self.__id_candidato = id_candidato_p
        self.__candidatos = list()
        self.__candidatos_bd = list()
        self.recuperar_candidatos()
        self.n_candidato = n_candidato

    # Atualiza o numero do candidato
    def set_id_candidato(self, id_candidato_p):
        self.__id_candidato = id_candidato_p

    # Atualiza a lista atual de candidatos
    def set_candidatos(self, candidatos_p):
        self.__candidatos = candidatos_p

    # Atualiza a lista dos candidatos vindos do Banco de Dados
    def set_candidatos_bd(self, candidatos_bd_p):
        self.__candidatos_bd = candidatos_bd_p

    def set_n_candidato(self, n_candidato):
        self.n_candidato = n_candidato

    def get_n_candidato(self):
        return self.n_candidato

    # Retorna o id do candidato
    def get_id_candidato(self):
        return self.__id_candidato

    # Retorna a lista dos candidatos da sessão atual
    def get_candidatos(self):
        return self.__candidatos

    # Retorna a lista dos candidatos vindos do Banco de Dados
    def get_candidatos_bd(self):
        return self.__candidatos_bd

    # Adiciona candidato à lista da sessão atual
    def add_candidato(self, candidato):
        self.__candidatos.append(candidato)

    # Adiciona candidato ao Banco de Dados
    def add_candidato_bd(self, candidato):
        inserir_candidato_bd(candidato)

    # Deleta candidato da sessão atual pelo CPF
    def deletar_candidato_id(self, id_candidato):
        index = 0
        for candidato in self.get_candidatos():
            if candidato.get_id_candidato() == id_candidato:
                self.get_candidatos().pop(index)
            index += 1

    # Remove o candidato do Banco de Dados
    def remover_candidato(self, id_candidato):
        self.deletar_candidato_id(id_candidato)
        deletar_candidato_bd(id_candidato)

    # Recupera os candidatos do Banco de Dados
    def recuperar_candidatos(self):
        candidatos = candidatos_bd()
        self.set_candidatos_bd(candidatos)
