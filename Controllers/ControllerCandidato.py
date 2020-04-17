from reliableVotinSystem.Models.Candidato import Candidato

class ControllerCandidato:
    def __init__(self):
        self.__candidato_model = Candidato()
        self.recovery_candidatos()

    # Retorna candidato pelo id
    def buscar_candidato(self, id_candidato):
        for candidato in self.get_model_candidato().get_candidatos():
            if candidato.get_id_candidato() == id_candidato:
                return candidato

    # Cadastra o candidato na lista da sessão atual
    def cadastrar_candidato_aux(self, nome_p, idade_p, cpf_p, sexo_p, titulo_p, id_candidato_p, n_candidato):
        candidato = Candidato(nome_p, idade_p, cpf_p, sexo_p, titulo_p, id_candidato_p)
        candidato.set_n_candidato(n_candidato)
        self.__candidato_model.add_candidato(candidato)

    # Cadastra o candidato no Banco de Dados e na sessão atual
    def cadastrar_candidato(self, nome_p, idade_p, cpf_p, sexo_p, titulo_p, id_candidato_p):
        if len(self.get_lista_candidatos()) > 0:
            n_candidato = self.get_lista_candidatos()[-1].get_n_candidato()+1
        else:
            n_candidato = 0
        candidato = Candidato(nome_p, idade_p, cpf_p, sexo_p, titulo_p, id_candidato_p, n_candidato)
        self.__candidato_model.add_candidato_bd(candidato)
        self.__candidato_model.add_candidato(candidato)

    # Remove o candidato da sessão atual e do Banco de Dados
    def remover_candidato(self, id_candidato):
        self.__candidato_model.remover_candidato(id_candidato)

    # Retorna o model de candidato
    def get_model_candidato(self):
        return self.__candidato_model

    # Recupera os candidatos vindos do Banco de Dados
    def recovery_candidatos(self):
        for att in self.__candidato_model.get_candidatos_bd():
            self.cadastrar_candidato_aux(att[0], att[1], att[2], att[3], att[4], att[5], att[6])

    def get_lista_candidatos(self):
        return self.get_model_candidato().get_candidatos()
