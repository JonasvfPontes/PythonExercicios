s=0
for c in range(0, 501, 3):
    if c%2 != 0:
        print(c, end=' ')
        s += c
print(f'\nA soma de todos os número ímpares multiplos de 3 é {s}')

