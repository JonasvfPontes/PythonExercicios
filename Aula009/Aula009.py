#Tratamento de caracteres
frase ='Jonas VasconCelos  de Freitas   pontes'

#Lembrando que o primeiro caractere ocupa a opsição 0 da string
#Letras maiúculas são diferentes de minusculas
print(f'\nOriginal: →→ {frase} ←←')
print(frase[9:13]) #mostrar do caractere 9 até o 13
print(len(frase)) #conta a qtde de caractere
print(frase.count('o')) #vai contar quantas vezez aparece a letra "o"
print(frase.count('o', 0, 13)) #contar num intervalo especifico, da posição 0 até 13
print(frase.find('onc')) #qual posição começa determinado caractere
print(frase.find('je')) #quando não encontra o método retorna -1
print('In→ ', 'Jonas' in frase) #In retorna True se houver o valor dentro da string, senão retona False

#Substituir uma sequecia de caractere por outra sequencia
print('replace:', frase.replace('Jonas', 'Jessica'))
print('Upper: ', frase.upper()) #Deixar todas maiúsculas
print('Lower: ', frase.lower()) #Deixar todas minúsculas
print('Captalize: ', frase.capitalize()) #Apenas o primeiro em maúcula
print('Title: ', frase.title()) #Todos os primeiros em maiúscula
print('Strip: ', frase.strip()) #Remove os apaços desnecessários no inicio e no fim da string
                                #tbm posso usar o 'rstrip' ou 'lstrip' o r e o l são respectivamente
                                #direita e esqueda, muitas funções no python possuem essas variações