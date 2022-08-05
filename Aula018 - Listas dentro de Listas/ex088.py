from random import randint
from time import sleep
jogo = []
print('_' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
numJogos = int(input('Quantos jogos vc quer que eu sorteie? '))
print(f' - - - Sorteando {numJogos} jogos - - -')
for c in range(0, numJogos):
    for cc in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in jogo:
                jogo.append(num)
                break
    jogo.sort()
    print(f'Jogo {c + 1}: {jogo}')
    sleep(0.5)
    jogo.clear()
print(f'\n\33[32m{"< BOA SORTE! >":*^30}\33[m')
