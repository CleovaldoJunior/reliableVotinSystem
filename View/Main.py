from reliableVotinSystem.Controllers.ControllerEleitor import *
from reliableVotinSystem.Models.Candidatos import Candidatos
from reliableVotinSystem.Models.Tabulacao import Tabulacao
from reliableVotinSystem.Banco import *

candidatos = Candidatos()
tabulacao = Tabulacao()
controllerEleitor = ControllerEleitor()
print(controllerEleitor.get_eleitor().get_eleitorado())
controllerEleitor.remover_eleitor("08502792407")
print(controllerEleitor.get_eleitor().get_eleitorado())

