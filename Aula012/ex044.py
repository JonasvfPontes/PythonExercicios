print('='*10,'LOJA DO JONAS','='*10)
p = float(input('Valor do produto: R$'))

print('''\n=======FORMA DE PAGAMENTO=======
À vista/Cheque \33[31m[1]\33[m  ---  Cartão Débito     \33[31m[2]\33[m
2x Cartão      \33[31m[3]\33[m  ---  3x ou mais Cartão \33[31m[4]\33[m''')
fp = int(input('Digite a opção de pagamento: '))
if fp == 1:
    x=0.9
    print(f'Valor com 10% de desconto R${p*x:.2f}')
elif fp == 2:
    x=0.95
    print(f'Valor com 5% de desconto R${p * x:.2f}')
elif fp ==3:
    x = 1
    print(f'Forma de pagamento SEM desconto R${p*x:.2f}')
else:
    x=1.2
    parcela = int(input('Em quantas vezes: '))
    print(f'Juros de 20% no montante, compra dividida em {parcela}x\nVlr final: \33[31mR${p*x:.2f}\33[m')