idade = cont_idade = cont_M = cont_F_menos20 = 0
sexo = opc = ''
while True:
    print('-'*20, '\nCADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip()[0]
    while sexo not in 'FfMm':
        sexo = input('\33[31mDigite apenas M ou F\33[m\nSexo: [M/F] ')
    if idade > 18:
        cont_idade += 1
    if sexo in 'mM':
        cont_M += 1
    if sexo in 'Ff' and idade < 20:
        cont_F_menos20 += 1
    print('-'*20)
    opc = input('Quer continuar? [S/N] ').strip()[0]
    while opc not in 'SsNn':
        opc = input('\33[31mOpção inválida\33[m\nQuer continuar? ')
    if opc in 'Nn':
        break
print('='*20)
print('\33[33mSegue relatório')
print(f'Temos {cont_idade} ', 'maiores' if cont_idade != 1 else 'maior' + 'de 18 anos')
print(f'Temos {cont_M}', ' homem' if cont_M == 1 else ' homens')
print(f'Temos {cont_F_menos20}', ' mulheres ' if cont_F_menos20 != 1 else ' mulher ' + 'com menos de 20 anos')

