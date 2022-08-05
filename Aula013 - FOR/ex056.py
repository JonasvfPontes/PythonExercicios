bdId = []
soma = 0
idadeHomemVelho = 0
nomeHomemVelho = ''
mulheresMenos20 = 0
for c in range(0, 4):
    nome = input(f'{c+1}º Nome ').strip()
    i = int(input(f'{c+1}ª Idade? '))
    sexo = input(f'{c+1}º Sexo [F] ou [M] ').strip()
    #Guardar o nome do homem mais velho
    if sexo.upper()=='M':
        if i > idadeHomemVelho:
            idadeHomemVelho = i
            nomeHomemVelho = nome
    else:
        if i < 20:
            mulheresMenos20 += 1
    #Add informações nas listas
    bdId.append(i) #Isso adiciona itens a uma lista
    print('=-'*5)
#Calcular média de idadades
for c in range(0, len(bdId)):
    soma += bdId[c]
media = soma/len(bdId)
#Imprimir resultados
print(f'A média de todo o grupo é {media}')
print(f'{nomeHomemVelho.capitalize()} tem {idadeHomemVelho} anos e é o homem mais velho!')
print(f'{mulheresMenos20} é a Qtde de mulheres com menos de 20 anos')

