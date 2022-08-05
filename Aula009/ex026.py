frase = input('Escrava algo: ').strip()
print('Sua frase tem {} lertas "A"'.format(frase.upper().count('A')))
print(f'A primeira aparece na posição {frase.upper().find("A")+1}')
print(f'A ultima a aparecer está na posição {frase.upper().rfind("A")+1}')
