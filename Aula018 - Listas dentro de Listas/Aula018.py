teste = []
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #Esses 2 pontos sever para fazer uma cópia e não uma ligação das duas listas
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
#outra forma de fazer uma lista dentro de outra lista
print('\nGalera 2 ↓↓')
galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera2)
print(galera2[0])
print(galera2[2][1])
print('\nPrintar com FOR')
for p in galera2:
    print(p)