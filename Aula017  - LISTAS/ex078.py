lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
menor = min(lista)
maior = max(lista)
print(f'Você digitou {lista}')
print(f'O maior valor é {maior} nas posições', end='')
for pos, v in enumerate(lista):
    if v == maior:
        print(f', {pos}', end='')
print(f'\nO menor valor é {menor} na posições', end='')
for pos, v in enumerate(lista):
    if v == menor:
        print(f', {pos}', end='')
