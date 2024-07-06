from Televisor import Televisor
from Controle import ControleRemoto

televisor = Televisor('SONY','SONY-123')

controle = ControleRemoto(televisor)

controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')

print(televisor.canal_atual)