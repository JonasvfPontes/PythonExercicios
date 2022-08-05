import random
pc = random.randint(0, 10)
n = int(input('Adivinha o número que estou pensando entre 0 e 10: '))
tentativas = 1
while n != pc:
    tentativas += 1
    print('Xiiii errooouuuuuu')
    n = int(input('Tente novamente '))
print(f'\nACERTOU!!!\nVc conseguiu na {tentativas}ª tentativa!')