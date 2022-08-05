
n = int(input('Digite um número inteiro: '))
opc = int(input('Diga para qual base quer que eu converta\n1 → Binário\n2 → Octal\n3 → Hexadecimal\n Digite uma opção: '))
if opc == 1:
    print(f'Opcção BINÁRIO: {bin(n)[2:]}')
elif opc == 2:
    print(f'Opção OCTAL: {oct(n)[2:]}')
elif opc ==3:
    print(f'Opção HEXADECIMAL: {hex(n)[2:]}')
else:
    print('\33[31mVc é burro, tente novamente')
