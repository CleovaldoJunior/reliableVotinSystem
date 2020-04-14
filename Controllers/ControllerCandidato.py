from reliableVotinSystem.Models.Candidato import Candidato

class ControllerCandidato:
    def __init__(self):
        self.candidato_model = Candidato()
        self.recovery_candidatos()

    def cadastrar_candidato_aux(self, nome_p, idade_p, cpf_p, sexo_p, titulo_p, id_candidato_p):
        candidato = Candidato(nome_p, idade_p, cpf_p, sexo_p, titulo_p, id_candidato_p)
        self.candidato_model.add_candidato(candidato)

    def cadastrar_candidato(self, nome_p, idade_p, cpf_p, sexo_p, titulo_p, id_candidato_p):
        candidato = Candidato(nome_p, idade_p, cpf_p, sexo_p, titulo_p, id_candidato_p)
        self.candidato_model.add_candidato_bd(candidato)
        self.candidato_model.add_candidato(candidato)

    def remover_candidato(self, id_candidato):
        self.candidato_model.remover_candidato(id_candidato)

    def get_model_candidato(self):
        return self.candidato_model

    def recovery_candidatos(self):
        for att in self.candidato_model.get_candidatos_bd():
            self.cadastrar_candidato_aux(att[0], att[1], att[2], att[3], att[4], att[5])