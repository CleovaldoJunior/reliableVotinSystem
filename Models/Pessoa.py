class Pessoa:

    def __init__(self, nome_p, idade_p, cpf_p, sexo_p):
        self.__nome = nome_p
        self.__idade = idade_p
        self.__cpf = cpf_p
        self.__sexo = sexo_p

    # Atualiza nome
    def set_nome(self, nomeP):
        self.__nome = nomeP

    # Atualiza idade
    def set_idade(self, idadeP):
        self.__idade = idadeP

    # Atualiza CPF
    def set_cpf(self, cpfP):
        self.__cpf = cpfP

    # Atualiza sexo
    def set_sexo(self, sexoP):
        self.__cpf = sexoP

    # Retorna nome
    def get_nome(self):
        return self.__nome

    # Retorna idade
    def get_idade(self):
        return self.__idade

    # Retorna CPF
    def get_cpf(self):
        return self.__cpf

    # Retorna sexo
    def get_sexo(self):
        return self.__sexo
