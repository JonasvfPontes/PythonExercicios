valores = list()
for c in range(0, 5):
    add = int(input('Digite um número '))
    if c == 0:
        valores.append(add)
    else:
      for pos, v in enumerate(valores):
        if v > add:
            valores.insert(pos, add)
            print(f'\33[31mFoi adicionado à posição {pos} da lista\33[m')
            break
        elif pos == len(valores) - 1:
            valores.append(add)
            print('\33[31mAdicionado ao final da lista\33[m')
            break
print('\33[1m_\33[m' * 30)
print(valores)
