palavras = ('jonas', 'jessica', 'helena', 'joao')
print('Mostrar as vogais nas palavras da TUPLA')
for p in palavras:
    print(f'\nNa palavra \33[32m{p.upper()}\33[m temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')


