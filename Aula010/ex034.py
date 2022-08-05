s = float(input('Qual o seu salário: '))
if s>1250:
    x = 1.1
else:
    x = 1.15
print(f'Seu novo salário com aumento de {(x-1)*100:.0f}% é R${s*x:.2f}')
