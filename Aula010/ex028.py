import random
al = random.randint(0, 5)
n = int(input('Adivinha o número que estou pensando entre 0 e 5: '))
if n == al:
    print('Sem... sal... cional brasil!!! PARABÉNS!')
else:
    print('Xiiii errooouuuuuu')
    print(f'Eu tinha pensado em {al}')
