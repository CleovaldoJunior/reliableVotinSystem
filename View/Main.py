from reliableVotinSystem.Models.Eleitor import Eleitor
from reliableVotinSystem.Models.Eleitorado import Eleitorado
from reliableVotinSystem.Models.Tabulacao import Tabulacao
from reliableVotinSystem.Models.Candidato import Candidato
from reliableVotinSystem.Models.Candidatos import Candidatos
from reliableVotinSystem.Controllers.ControllerTabulacao import *

candidatos = Candidatos()
tabulacao = Tabulacao()
eleitorado = Eleitorado()

lais = Eleitor("Lais", "18", "cpf", "F", "159")
junior = Eleitor("Junior", "19", "333", "M", "789")

bolsonaro = Candidato("Bolsonaro", "64", "cpf", "M", "157", "17")
lula = Candidato("Lula", "69", "cpf", "M", "111", "13")
cabo_daciolo = Candidato("Cabo Desse o Rolo", "50", "cpf", "M", "000", "51")

candidatos.add_candidato(bolsonaro)
candidatos.add_candidato(lula),
candidatos.add_candidato(cabo_daciolo)
eleitorado.add_eleitor(lais)
eleitorado.add_eleitor(junior)

junior.votar("13", tabulacao)

for i in tabulacao.get_votos():
    x = buscar_candidato(i.get_n_candidato(), candidatos.get_candidatos())
    print("Voto em "+x.get_nome() if x != None else "None" )
