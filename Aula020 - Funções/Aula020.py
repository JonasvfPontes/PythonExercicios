def lin():
    print('-' * 30)


lin() #Sempre que houver uma DEF o python pede que dê 2 linhas brancas de espaço
print('   Isso é um teste')
lin()
print('   Aprenda Python')
lin()


print('\33[31m_\33[m' * 40)
# Também podemos fazer um seguinte
def mensagem(escrevaSuaMensagem): #Criei uma DEF mensagem com uma variável "escrevaSuaMensagem"
    print('-' * 30)
    print(escrevaSuaMensagem) #Aqui estou dizendo que é para imprimir o valor que "escrevaSuaMensagem" vai receber
    print('-' * 30)


mensagem('        jonas')

print('\33[31m_\33[m' * 40)
def soma(a, b):
    print(f'A= {a}, B={b} = ', a + b)


soma(4, 5)
soma(a=1, b=0)
soma(b=6, a=2)

print('\33[31m_\33[m' * 40)
def somar(* valores):
    s = 0
    for v in valores:
        s += v
    print(f'Somando os valores {valores} dá {s} ')


somar(5, 6, 7)