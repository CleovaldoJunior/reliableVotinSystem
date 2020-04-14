from reliableVotinSystem.Controllers.ControllerEleitor import *
from reliableVotinSystem.Controllers.ControllerCandidato import *

controllerCandidato = ControllerCandidato()
controllerEleitor = ControllerEleitor()
print(controllerCandidato.get_model_candidato().get_candidatos())
print(controllerEleitor.get_model_eleitor().get_eleitorado()[0].get_nome())






