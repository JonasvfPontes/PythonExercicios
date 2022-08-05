def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura:.1f} x {comprimento:.1f} é de {a:.1f}m²')


print('Controle de Terrenos')
print('_____________________')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
