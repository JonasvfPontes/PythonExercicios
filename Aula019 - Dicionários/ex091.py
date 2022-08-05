from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
print('Valores sorteados')
jogadores["jogador1"] = randint(1, 6)
jogadores["jogador2"] = randint(1, 6)
jogadores["jogador3"] = randint(1, 6)
jogadores["jogador4"] = randint(1, 6)
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('Ranking dos jogadores:')

ranking = []
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) #Coloquei o dicinário dentro de uma lista
for v, i in enumerate(ranking):
    print(f'{v + 1}º lugar: {i[0]} com {i[1]}')
    sleep(1)