#Exemplo de como usar uma lista temporárea para preencher outra "permanente"
bd = list()
dados = list()
for c in range(0, 3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade:  ')))
    bd.append(dados[:])
    dados.clear()
print(bd)
