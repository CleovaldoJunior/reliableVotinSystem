from reliableVotinSystem.Controllers.ControllerEleitor import *
from reliableVotinSystem.Controllers.ControllerCandidato import *
from reliableVotinSystem.Controllers.ControllerTabulacao import *

controllerTabulacao = ControllerTabulacao()
controllerCandidato = ControllerCandidato()
controllerEleitor = ControllerEleitor()

listaCandidatos = controllerCandidato.get_lista_candidatos()
listaEleitorado = controllerEleitor.get_lista_eleitorado()

listaEleitorado[0].votar(listaCandidatos[0].get_id_candidato(), controllerTabulacao.get_model_tabulacao())
listaEleitorado[1].votar(listaCandidatos[0].get_id_candidato(), controllerTabulacao.get_model_tabulacao())

for i in listaEleitorado:
    print(i.get_cipher_vote())









