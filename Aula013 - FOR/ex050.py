s=0
for c in range(0,6):
    i = int(input('Digite um número '))
    if i%2 == 0:
        s += i
print(f'A soma de todos os PARES é {s}')