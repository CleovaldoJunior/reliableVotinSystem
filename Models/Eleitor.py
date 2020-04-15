from reliableVotinSystem.Models.Pessoa import Pessoa
from reliableVotinSystem.Models.Voto import Voto
from reliableVotinSystem.Security.RSA import *
from reliableVotinSystem.Banco import *


class Eleitor(Pessoa):

    def __init__(self, nome_p=None, idade_p=None, cpf_p=None, sexo_p=None, titulo_p=None):
        super().__init__(nome_p, idade_p, cpf_p, sexo_p)
        self.__titulo = titulo_p
        self.__eleitorado = list()
        self.__eleitorado_bd = list()
        self.__cipher_vote = None
        self.__public_key = get_keys(256)[0]
        self.recuperar_eleitorado()

    # Atualiza o titulo de eleitor
    def set_titulo(self, titulo_p):
        self.__titulo = titulo_p

    # Atualiza a lista dos eleitores vindos do Banco de Dados
    def set_eleitorado_bd(self, eleitorado_p):
        self.__eleitorado_bd = eleitorado_p

    # Atualiza a lista dos eleitores atuais, incluindo os cadastrados na sessão
    def set_eleitorado(self, eleitores_p):
        self.__eleitorado = eleitores_p

    # Retorna o titulo de eleitor
    def get_titulo(self):
        return self.__titulo

    # Retorna a lista dos eleitores na sessão atual
    def get_eleitorado(self):
        return self.__eleitorado

    # Retorna a lista dos eleitores vindos do Banco de Dados
    def get_eleitorado_bd(self):
        return self.__eleitorado_bd

    def get_cipher_vote(self):
        return self.__cipher_vote

    def get_public_key(self):
        return self.__public_key

    # Eleitor vota em algum candidato
    def votar(self, n_candidato, tabulacao):
        voto = Voto(n_candidato, self.get_titulo(), self.get_public_key())
        self.__cipher_vote = voto.get_cipher_vote()
        tabulacao.aplicar_voto(voto)

    # Deleta o eleitor da lista da sessão atual pelo CPF
    def deletar_eleitor_cpf(self, cpf):
        index = 0
        for eleitor in self.get_eleitorado():
            if eleitor.get_id_candidato() == cpf:
                self.get_eleitorado().pop(index)
            index += 1

    # Adiciona eleitor à lista da sessão atual
    def add_eleitor(self, eleitor):
        self.__eleitorado.append(eleitor)

    # Adiciona eleitor ao Banco de Dados
    def add_eleitor_bd(self, eleitor):
        inserir_eleitor_bd(eleitor)

    # Remove eleitor do Banco de Dados
    def remover_eleitor_bd(self, eleitor):
        deletar_eleitor_bd(eleitor)

    # Recupera os eleitos do Banco de Dados
    def recuperar_eleitorado(self):
        eleitores = eleitores_bd()
        self.set_eleitorado_bd(eleitores)
