valores = [8, 2, 5, 4, 9, 3, 0]
maisValores = list(range(4, 11))
print(valores)
print(maisValores)

print('\n\33[32mADICIONAR ELEMENTOS\33[m')
maisValores.append(5) #APPEND adiciona valores ao final da lista
print('\nAPPEND "5" ↓')
print(maisValores)
maisValores.insert(7, 'Olá') #Adiciona elementos numa lista, nesse caso, na posição 7 adicinar o número "Olá"
print('insert(7, "Olá")  ↓↓')
print(maisValores)

print('\n\33[31mREMOVER ELEMENTOS\33[m')
print('\n POP ↓')
maisValores.pop() #Remore o ultimo item da lista
print(maisValores)
maisValores.pop(4) # porém tbm posso adicionar a posição que quero remover
print('POP(4) ↓')
print(maisValores)
del maisValores[0] #Remover item específico da lista
print('DEL maisValores[0]')
print(maisValores)
maisValores.remove('Olá') #Remove o item descrito no método, nesse caso ele vai remover "olá" indempente da posição
print('.remove("Olá")') #Se tentar remover algo que não existe na lista esse comando retornará ERROR
print(maisValores)

print('\n\33[34mORGANIZAR ELEMENTOS\33[m')
valores.sort() #Organiza a ordem dos itens dentro da lista
print('valores.sort() ↓')
print(valores)
valores.sort(reverse=True)
print('valores.sort(reverse=True) ↓↓↓') #ordena do maior para o menor
print(valores)