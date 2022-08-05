#declarar um dicinário pode ser assim
#exemplo = dict() ou ↓
exemplo = {'Nome':'Pedro', 'idade':25}
print(exemplo['Nome'])
print(exemplo['idade'])
#Para criar mais um "cabeçalho" num dicionário basta fazer assim ↓
exemplo['sexo'] ='M'
print(exemplo['sexo'])

#Para remover um "cabeçalho" num dicionário basta fazer assim ↓
del exemplo['idade']
print(exemplo)

print('\nFILME: ↓↓↓')
#Outra forma de criar um dicinoário é:
filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
         }
print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())
