preço = soma = cont_acima_de_mil = menor_valor = 0
nome = nome_menor_valor = ''
opc = ' '
faixada = 'LOJA SUPER BARATÃO'
print('\33[1m-'*30)
print(f'\33[34m{faixada:^30}\33[m')
print('\33[1m-\33[m'*30)
while True:
    nome = input('Nome do produto: ').strip()
    preço = float(input('Preço: R$'))
    opc = ' '
    soma += preço
    if preço > 1000:
        cont_acima_de_mil += 1
    if menor_valor == 0:
        menor_valor = preço
        nome_menor_valor = nome
    elif preço < menor_valor:
        menor_valor = preço
        nome_menor_valor = nome
    while opc not in 'SsNn':
        opc = input('Quer adicionar mais? [S/N] ').strip()[0]
    if opc in 'Nn':
        break
print(f'\nO total gasto nessa compra é R${soma:.2f}')
print(f'Você comprou {cont_acima_de_mil}', 'produto' if cont_acima_de_mil == 1 else 'produtos', 'acima de mil reais')
print(f'O nome do produto mais barato é: \33[31m{nome_menor_valor.upper()}\33[m')
