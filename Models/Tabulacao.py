class Tabulacao:

    def __init__(self):
        self.__votos = list()

    def aplicar_voto(self, voto):
        self.get_votos().append(voto)

    def get_votos(self):
        return self.__votos
