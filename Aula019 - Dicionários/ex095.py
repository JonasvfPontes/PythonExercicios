time = []
jogador = {}
gols = []
while True:
    jogador["nome"] = input('Nome do jogador: ').strip().capitalize()
    QtdePartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, QtdePartidas):
        gols.append(int(input(f'    Quantos gols na {c + 1}ª partida? ')))
    jogador["gols"] = gols[:]
    jogador["total"] = sum(gols)
    gols.clear()
    time.append(jogador.copy())
    #EU NÃO LIMPEI O DICIONÁRIO JOGADOR PORQUE QUANDO DÁ O LOOP EU SEMPRE ESTOU SUBSTITUINDO INFORMAÇÃO
    #E NÃO ADICIONANDO NOVAS AO DICINOÁRIO
    opc = ' '
    while True:
        opc = input('Quer continuar? [S/N] ').strip().upper()[0]
        if opc not in 'SN':
            print('ERRO! Digite apenas S ou N')
        else:
            break
    if opc == 'N':
        break
print('=' * 35)
print('Cod/Nome      Gols          Total')
print('-' * 35)
for v, i in enumerate(time):
    print(f'{v} {i["nome"]:<11} {str(i["gols"]):<15} {i["total"]}')
print('-' * 35)
while True:
    opc = int(input('Mostrar dados de qual jogagor? (999 para parar) '))
    if opc == 999:
        break
    elif opc >= len(time):
        print(f'\33[31mERRO! Digite uma opçãop de 0 à {len(time) - 1}\33[m')
    else:
        print(f'\33[34m-- LEVANTAMENTO DO JOGAGOR {time[opc]["nome"]}:')
        if opc == 999:
            break
        else:
            for v, i in enumerate(time[opc]["gols"]):
                print(f'        No jogo {v + 1} fez {i} gols.')
            print('\33[m')
