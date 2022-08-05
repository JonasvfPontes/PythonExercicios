valores = list()
while True:
    opc = ' '
    valores.append(int(input('Digite um valor: ')))
    while opc not in 'sn':
        opc = input('Quer continuar? [s/n] ').strip().lower()[0]
    if opc == 'n':
        break
print(f'Você digitou {len(valores)} valores')
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print(f'O número 5 está na lista digitada, na posiçao {valores.index(5)}')
else:
    print('O valor 5 não foi encontrado')
