cadastro = {"Nome":[], "Sexo":[], "Idade":[]}
while True:
    cadastro["Nome"].append(input('Nome: ').strip().capitalize())
    while True:
        sexo = input('Sexo: [M/F] ').strip().upper()
        if sexo not in 'MF':
            print('ERRO! Digite apenas M ou F.')
        else:
            cadastro["Sexo"].append(sexo)
            break
    cadastro["Idade"].append(float(input('Idade: ')))
    while True:
        opc = ' '
        opc = input('Quer continuar? [S/N] ')
        if opc not in 'sn':
            print('ERRO! Digite apenas S ou N')
        else:
            break
    if opc == 'n':
        break
print('=' * 30)
print(f'A) Ao todo temos {len(cadastro["Nome"])} pessoas cadastradas')
média = sum(cadastro["Idade"])/len(cadastro["Idade"])
print(f'B) A média de idade é de {média:.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for k, v in enumerate(cadastro["Sexo"]):
    if v == 'F':
        print(cadastro["Nome"][k], end=' ')
print()
print(f'D) lista de pessoas acima da média de idade: ')
for i, v in enumerate(cadastro["Idade"]):
    if v >= média:
        print(f'\33[32mNome:\33[m {cadastro["Nome"][i]};\33[32m Sexo:\33[m {cadastro["Sexo"][i]};\33[32m Idade:\33[m {cadastro["Idade"][i]}')
print('<<< ENCERRADO >>>')
