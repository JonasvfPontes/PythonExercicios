soma = 0
cont = 0
opc = ''
num = int(input('Digite um número '))
maior = num
menor = num

while opc != 'N':
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    cont += 1
    opc = ''
    while opc != 'S' and opc != 'N':
        opc = input('Quer continuas? [S]/[N] ').upper()
        if opc != 'S' and opc != 'N':
            print('\33[31mEscolha uma das opções...\33[m ')
    if opc == 'S':
        num = int(input('Ok, digte um número: '))
print(f'\33[32m\nA média é {soma/cont}\nO mario número foi {maior}\nO menor número foi {menor}\33[m')
