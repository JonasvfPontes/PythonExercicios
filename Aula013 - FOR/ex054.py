maior=0
menor=0
# Considerando 21 como a maior idade
for c in range(0,7):
    i = int(input(f'Digite a {c+1}ª idade: '))
    if i >= 21:
        maior += 1
    else:
        menor += 1
print(f'''
Destes posso afirma que
{maior} são MAIORES DE IDADE e
{menor} são MENORES DE IDADE ''')