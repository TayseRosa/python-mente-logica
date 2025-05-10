#Modulos
## Os que estão no Pyhton = importa
## Os que NÃO estão no Pyhton = Instala com gerenciador de dependências pip

import math
numero = 16
raiz_quadrada = math.sqrt(numero)
print(f"A raiz quadrada de {numero} é {raiz_quadrada}")

from math import pi
print(f"O valor do pi é {pi}")

#Numeros randomicos
import random
dado = random.randint(1,6)
print(f"O numero do dado é: {dado}")

#Datas
from datetime import datetime
agora = datetime.now()
print(f"A hora atual é: {agora}")

#Sistema Operacional
import os
arquivos = os.listdir('.')
# . = diretorio atual
print(f'Os arquivos dessa pasta são: {arquivos} ')

import sys
print(f"A versao do Pyhton é {sys.version}")