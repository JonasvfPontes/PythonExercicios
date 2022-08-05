expressao = input('Digite a expressão: ').strip()
lista = list()
for v in expressao:
    lista.append(v)
abrir = lista.count('(')
fechar = lista.count(')')
print(lista)
if lista.index(')') < lista.index('('):
    print('Sua expressçao está \33[31mERRADA!\33[m')
    print('Você não pode iniciar com o parentese de fechar')
elif abrir == fechar:
    print('Sua expressão está \33[32mCORRETA!\33[m')
else:
    print('Sua expressçao está \33[31mERRADA!\33[m')

