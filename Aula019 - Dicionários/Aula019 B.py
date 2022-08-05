from random import randint
from time import sleep
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
cont = 1
while True:
    maior = max(jogadores.values())
    for k, v in jogadores.items():
        if v == maior:
            print(f'{cont}º lugar: {k} com {v}')
            del k
            cont += 1
            break
        if len(jogadores) == 0:
            break
