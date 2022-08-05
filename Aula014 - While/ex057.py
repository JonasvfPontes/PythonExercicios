sexo = input('Digite seu sexo: ').upper()
if sexo == 'M' or sexo == 'F':
    print('', end='')
else:
    while sexo != 'M' and sexo != 'F':
        sexo = input('Tente novamente, apenas [M] ou [F]: ').upper()
print('Fim')