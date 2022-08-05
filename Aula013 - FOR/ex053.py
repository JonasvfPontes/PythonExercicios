frase = input('Digite uma frase: ').split()
tudo = str('')
i = len(frase)
for c in range(0, i):
    tudo += frase[c]
#uma forma de inverter uma string é "string[::-1]
if tudo==tudo[::-1]:
    print('Essa frase é um PALÍNDROMO')
else:
    print('Essa frase \33[31mnão é um PALÍNDROMO\33[m')