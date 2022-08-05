lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche[0])
print(lanche[:2])
print(lanche[-2])
print(lanche[-2:])
print(lanche[:-2], '\n')

#----------------------------------------------------------------------
#Se quiser mostrar item por item, ou usar num texto pode usar um FOR ↓
for c in lanche:
    print(f'Irei comer um {c}')
print('\33[31mComi demais!\n\33[m')

#Mostrar de forma ordenada
print('Mostrar de forma ordenada')
print(sorted(lanche))

#Métodos numa TUPLA
print('-'*30)
a = 2, 5, 8
b = 9, 1, 5, 3
c = a + b
print(a)
print(c)

#Método COUNT, Conta quantas vez algo aparce
print(c.count(5), ' - isso mostra que o número 5 aparece 2 vezes na tupla C')

#Método INDEX, Conta quantas vez algo aparce
print(c.index(3), '- isso mostra em qual posição está o termo procurado, nesse caso o número 3')