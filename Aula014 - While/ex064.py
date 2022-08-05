n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número int '))
    if  n != 999:
        soma += n
        cont += 1
print(f'\nVocê digitou {cont} números\nA soma de todos é {soma}')
