aluno = {"Nome":'', "Média":''}
aluno["Nome"] = input('Nome: ').capitalize().strip()
aluno["Média"] = float(input(f'Média de {aluno["Nome"]} '))
print(f'Nome é igual a {aluno["Nome"]}')
print(f'A média é igual a {aluno["Média"]}')
print('Situação é igual a ', end='')
if aluno["Média"] >= 6:
    print('APROVADO! ☻')
else:
    print('REPROVADO!')
