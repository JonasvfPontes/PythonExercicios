num = (int(input('Digite um núemro: ')),
       int(input('Digite outro núemro: ')),
       int(input('Digite mais um núemro: ')),
       int(input('Digite o ultimo núemro: ')))
épar = 0
numPar = ''
for c in num:
    if c % 2 == 0:
        numPar += str(f'{c} ')
        épar += 1
print(f'O número 9 aparece {num.count(9)}', 'vez' if num.count(9) == 1 else 'vezes')
try:
    posição = num.index(3)
except:
    posição = 0
print(f'O número 3 aparece na posição {posição + 1} pela primeira vez' if posição != 0 else 'O número 3 não existe nessa TUPLA')
print(f'Temos {épar}', 'número par' if épar == 1 else 'números pares')
print(f'\33[35m({numPar.strip()})')
