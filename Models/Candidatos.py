class Candidatos:

    def __init__(self):
        self.__candidatos = list()

    def add_candidato(self, Candidato):
        self.__candidatos.append(Candidato)

    def get_candidatos(self):
        return self.__candidatos

    def set_candidatos(self, candidatos_p):
        self.__candidatos = candidatos_p