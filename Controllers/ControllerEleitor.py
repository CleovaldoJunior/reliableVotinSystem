from reliableVotinSystem.Models.Eleitor import Eleitor


class ControllerEleitor:
    def __init__(self):
        self.__eleitor_model = Eleitor()
        self.recovery_eleitorado()

    # Retorna eleitor pelo cpf
    def buscar_eleitor_cpf(self, cpf):
        for eleitor in self.get_model_eleitor().get_eleitorado():
            if eleitor.get_cpf() == cpf:
                return eleitor

    # Cadastra o eleitor na lista da sessão atual
    def cadastrar_eleitor_aux(self, nome_p, idade_p, cpf_p, sexo_p, titulo_p):
        eleitor = Eleitor(nome_p, idade_p, cpf_p, sexo_p, titulo_p)
        self.__eleitor_model.add_eleitor(eleitor)

    # Cadastra o eleitor no Banco de Dados e na sessão atual
    def cadastrar_eleitor(self, nome_p, idade_p, cpf_p, sexo_p, titulo_p):
        eleitor = Eleitor(nome_p, idade_p, cpf_p, sexo_p, titulo_p)
        self.__eleitor_model.add_eleitor_bd(eleitor)
        self.__eleitor_model.add_eleitor(eleitor)

    # Remove o eleitor da sessão atual e do Banco de Dados
    def remover_eleitor(self, cpf):
        self.__eleitor_model.remover_eleitor_bd(cpf)
        self.__eleitor_model.deletar_eleitor_cpf(cpf)

    # Retorna o model de eleitor
    def get_model_eleitor(self):
        return self.__eleitor_model

    # Recupera os eleitores vindos do Banco de Dados
    def recovery_eleitorado(self):
        for att in self.__eleitor_model.get_eleitorado_bd():
            self.cadastrar_eleitor_aux(att[0], att[1], att[2], att[3], att[4])

    def get_lista_eleitorado(self):
        return self.get_model_eleitor().get_eleitorado()
