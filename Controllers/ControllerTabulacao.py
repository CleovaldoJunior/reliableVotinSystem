from reliableVotinSystem.Models.Tabulacao import *

class ControllerTabulacao:
    def __init__(self):
        self.__model_tabulacao = Tabulacao()

    def get_model_tabulacao(self):
        return self.__model_tabulacao

    def get_lista_votos(self):
        return self.get_model_tabulacao().get_votos()