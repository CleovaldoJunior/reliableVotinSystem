class Eleitorado:

    def __init__(self):
        self.__eleitores = list()

    def add_eleitor(self, Eleitor):
        self.__eleitores.append(Eleitor)

    def get_eleitorado(self):
        return self.__eleitores

    def set_eleitorado(self, eleitores_p):
        self.__eleitores = eleitores_p