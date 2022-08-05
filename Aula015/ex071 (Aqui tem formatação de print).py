while True:
    valor = int(input('Valor para saque: R$'))
    n50 = int(valor / 50)
    n20 = int((valor - n50 * 50) / 20)
    n10 = int((valor - n50 * 50 - n20 * 20) / 10)
    n1 = int(valor - n50 * 50 - n20 * 20 - n10 * 10)
    break
print('='*30)
print(f'''
Total de {n50} cédulas de R$ 50
Total de {n20} cédulas de R$ 20
Total de {n10} cédulas de R$ 10
total de {n1} cédulas de R$ 1\n''')
print('='*30)
banco = 'Volte sempre ao banco JP'
print(f'\33[33m{banco:-^30}\33[m')
