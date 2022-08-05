from math import sqrt
co = float(input('Valor do cateto oposto '))
ca = float(input('Valor do cateto adjacente '))
hp = sqrt(ca**2 + co**2)
print(f'O valor da hipotenusa é {hp:.2f}')
