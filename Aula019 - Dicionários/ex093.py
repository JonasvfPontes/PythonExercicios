jogador = {"Nome":'', "Gols":[]}
jogador["Nome"] = input('Nome do jogador: ').strip().capitalize()
p = int(input(f'Quatas partidas o {jogador["Nome"]} jogou? '))
for c in range(0, p):
    jogador["Gols"].append(int(input(f'Quantos gols na {c +1}ª partida? ')))
jogador["Total"] = sum(jogador["Gols"])
print('=' * 30)
print(jogador)
print('=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])}', "partidas" if not len(jogador["Gols"]) == 1 else "partida")
for v, i in enumerate(jogador["Gols"]):
    print(f' → Na partida {v + 1}, fez {i} gols.')
print(f'Foi o total de {jogador["Total"]}')
