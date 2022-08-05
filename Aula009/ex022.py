#Video 31

nome = input('Digite seu nome: ')
print(nome.upper())
print(nome.lower())
dividido = nome.split()
print('Temos {} caracteres, sem contar espaços'.format(len(nome) - nome.count(' ')))
print(f'A primeira palavra tem {len(dividido[0])} caracteres')

