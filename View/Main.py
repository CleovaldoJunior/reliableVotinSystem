from reliableVotinSystem.Controllers.ControllerEleitor import *
from reliableVotinSystem.Controllers.ControllerCandidato import *
from reliableVotinSystem.Models.Tabulacao import Tabulacao

controllerCandidato = ControllerCandidato()
controllerEleitor = ControllerEleitor()
print(controllerCandidato.get_model_candidato().get_candidatos())






