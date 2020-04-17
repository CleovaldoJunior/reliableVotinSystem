from reliableVotinSystem.Models.third_party import *
from reliableVotinSystem.Security.Paillier_Cipher import *
class ControllerThirdParty():
    def __init__(self):
        self.model_tp = Third_party()

    def tallying(self, lista_votos):
        print(decrypt_list(lista_votos))