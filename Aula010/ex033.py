n1 = float(input('Digite um número '))
n2 = float(input('Agora outro '))
n3 = float(input('Só mais essa vez '))
x=n1
#---
if n2 > x:
    x = n2
if n3 > x:
    x = n3
#----
y = n1
if n2 < y:
    y = n2
if n3 < y:
    y = n3

print(f'O maior número é {x}\ne o menor número é {y}')
