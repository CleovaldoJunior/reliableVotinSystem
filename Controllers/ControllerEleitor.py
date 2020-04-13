from reliableVotinSystem.Models.Eleitor import Eleitor

class ControllerEleitor:
    def __init__(self):
        self.eleitor_model = Eleitor()
        self.recovery_eleitorado()

    def cadastrar_eleitor(self, nome_p, idade_p, cpf_p, sexo_p, titulo_p):
        eleitor = Eleitor(nome_p, idade_p, cpf_p, sexo_p, titulo_p)
        self.eleitor_model.add_eleitor(eleitor)

    def cadastrar_eleitor_bd(self, nome_p, idade_p, cpf_p, sexo_p, titulo_p):
        eleitor = Eleitor(nome_p, idade_p, cpf_p, sexo_p, titulo_p)
        self.eleitor_model.add_eleitor_bd(eleitor)
        self.eleitor_model.add_eleitor(eleitor)

    def remover_eleitor(self, cpf):
        self.eleitor_model.remover_eleitor(cpf)

    def get_eleitor(self):
        return self.eleitor_model

    def recovery_eleitorado(self):
        for att in self.eleitor_model.get_eleitorado_bd():
            self.cadastrar_eleitor(att[0], att[1], att[2], att[3], att[4])