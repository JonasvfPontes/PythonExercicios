valores = list()
par = list()
impar = list()
while True:
    opc = ' '
    add = int(input('Digite um valor: '))
    valores.append(add)
    if add % 2 == 0:
        par.append(add)
    else:
        impar.append(add)
    while opc not in 'sn':
        opc = input('Quer continuar? [s/n] ').strip().lower()[0]
    if opc == 'n':
        break
print('-'*30)
print(valores)
print(f'Os valores PARES são {par}')
print(f'Os valores ÍMPARES são {impar}')
