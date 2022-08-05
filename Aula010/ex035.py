'''   Desenvolva um programa que leia o
valor de 3 retas e diga se dá pra formar um
triângulo juntando-os'''
print('***' * 15)
r1 = float(input('Primeira reta '))
r2 = float(input('Segunda reta '))
r3 = float(input('Terceira reta '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas formam um triângulo')
else:
    print('Infelismente não dá pra formar um triângulo')
#Próxima aula será vídeo 46