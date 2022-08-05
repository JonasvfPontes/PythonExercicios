bd = list()
dado = list()
listaPesado = list()
listaLeve = list()
pesado = 0
leve = 0
print('_' * 30)
print(f'{"Cadastro de pessoas":^30}')
print('-' * 30)
while True:
    dado.append(input('Nome: '))
    dado.append(int(input('Peso: ')))
    bd.append(dado[:])
    dado.clear()
    opc = ' '
    while opc not in 'sn':
        opc = input('Quer continuar? ').strip().lower()[0]
    if opc == 'n':
        break
print('\33[31m_\33[m' * 30)
print(f'Você cadastrou {len(bd)} pessoas')
cont = 0
pesado = max(bd)
for c in bd:
    if cont == 0:
        pesado = leve = c[1]
    else:
        if c[1] > pesado:
            pesado = c[1]
        if c[1] < leve:
            leve = c[1]
    cont += 1
print(f'As mais pesadas tem {pesado}Kg e são ', end='')
for c in bd:
    if c[1] == pesado:
        listaPesado.append(c[0].capitalize())
print(listaPesado)
print(f'As mais leves tem {leve}Kg e são ', end='')
for c in bd:
    if c[1] == leve:
        listaLeve.append(c[0].capitalize())
print(listaLeve)
