import binascii

from reliableVotinSystem.Controllers.ControllerEleitor import *
from reliableVotinSystem.Controllers.ControllerCandidato import *
from reliableVotinSystem.Controllers.ControllerTabulacao import *
from reliableVotinSystem.Models.Voto import *

controllerTabulacao = ControllerTabulacao()
controllerCandidato = ControllerCandidato()
controllerEleitor = ControllerEleitor()

listaCandidatos = controllerCandidato.get_lista_candidatos()
listaEleitorado = controllerEleitor.get_lista_eleitorado()
print(listaEleitorado)
print(listaCandidatos)
for i in listaCandidatos:
    print(i.get_n_candidato())










