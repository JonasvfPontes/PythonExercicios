i = int(input('Digite um número '))
qtde_Divisível = 0
status = ''
for c in range(1, i):
    if i % c == 0:
        qtde_Divisível += 1
    if qtde_Divisível > 2:
        status = 'NÃO '
        c = i
print(f'{i} {status}é primo')
