def leiaInt(txt):
    while True:
        num = input(txt).strip()
        if num.isnumeric():
            if (float(num) - int(num)) > 0:
                print(f'\33[31mERRO! Digite um número inteiro válido.\33[m')
            else:
                return num
                break
        else:
            print(f'\33[31mERRO! Digite um número inteiro válido.\33[m')

print('_' * 30)
n = leiaInt('Digite um número: ')
print(f'Você digitou {n}')
x = leiaInt('Digite outro número: ')
print(f'PRONTO, vc digitou {x}')
