def ficha(jogador='', gols=0):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


print('_' * 30)
j = input('Nome do jogador: ')
g = input('Número de Gols: ')
ficha(j, g)
