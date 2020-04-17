from reliableVotinSystem.Controllers.ControllerThirdParty import *
from reliableVotinSystem.Controllers.ControllerEleitor import *
from reliableVotinSystem.Controllers.ControllerCandidato import *
from reliableVotinSystem.Controllers.ControllerTabulacao import *

controllerTabulacao = ControllerTabulacao()
controllerCandidato = ControllerCandidato()
controllerEleitor = ControllerEleitor()
controllerTp = ControllerThirdParty()

listaCandidatos = controllerCandidato.get_lista_candidatos()
listaEleitorado = controllerEleitor.get_lista_eleitorado()
listaEleitorado[0].votar(1, controllerTabulacao.get_model_tabulacao())
listaEleitorado[0].votar(2, controllerTabulacao.get_model_tabulacao())
listaEleitorado[0].votar(6, controllerTabulacao.get_model_tabulacao())
listaEleitorado[0].votar(8, controllerTabulacao.get_model_tabulacao())
listaEleitorado[0].votar(9, controllerTabulacao.get_model_tabulacao())
listaEleitorado[0].votar(5, controllerTabulacao.get_model_tabulacao())
listaEleitorado[0].votar(9, controllerTabulacao.get_model_tabulacao())
listaEleitorado[0].votar(9, controllerTabulacao.get_model_tabulacao())
listaEleitorado[0].votar(9, controllerTabulacao.get_model_tabulacao())
controllerTp.tallying(controllerTabulacao.get_lista_votos())












