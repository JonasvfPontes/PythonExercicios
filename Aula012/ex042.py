print('***' * 15)
r1 = float(input('Primeira reta '))
r2 = float(input('Segunda reta '))
r3 = float(input('Terceira reta '))
x=0
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\n\033[7;32mEssas retas formam um triângulo\033[m')
    x=1
else:
    print('\33[0;31mInfelismente não dá pra formar um triângulo\33[m')

if x==1:
    if r1==r2 and r2==r3:
        print('E digo mais, esse é EQUILÁTERO')
    elif r1==r2 and r1!=r3 or r1==r3 and r1!=r2 or r2==r3 and r2!=r1 :
        print('Esse triangulo é ISÓSCELES')
    else:
        print('Esse bicho é ESCALENO')
