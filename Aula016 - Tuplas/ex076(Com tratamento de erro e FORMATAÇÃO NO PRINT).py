estoque = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.9)
print('_'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_'*40)
for c in estoque:
    try: #É como se fosse um SEERRO do Python
        c.isalpha()
        print(f'{c:.<30}', end='R$ ')
    except: #Segunda parte do "SEERRO"
      print(f'{c:>7.2f}')
print('_'*40)


