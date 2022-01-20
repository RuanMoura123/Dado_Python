from random import randint  # Importei o "random"
from time import sleep  # Importei o time (demora na apresentação do resultado)
from operator import itemgetter
# Abrir chave {} significa abrir um dicionário.

jogo = {"jogador1": randint(1, 6),
        "jogador2": randint(1, 6),
        "jogador3": randint(1, 6),
        "jogador4": randint(1, 6)}

"""
Ao importar o 'random' import randint eu consigo sortear
números aleatórios de acordo com o mínimo e máximo sele-
cionado.

Dessa forma eu consigo realizar o dado.
"""

print(jogo)

ranking = list()

print("Valores Sorteados: ")
for k, v in jogo.items():
        print(f'{k} tirou {v} no dado.')
        sleep(0.5)

ranking = sorted(jogo.items(), key=itemgetter(1))

"""
O K e o V significa chave e fechadura
"""
print("               ====RANKING DOS JOGADORES==== ")

print("", ranking)
for i, v in enumerate(ranking):
        print(f'{i+1} lugar: {v[0]} com {v[1]}.')
        sleep(1)
