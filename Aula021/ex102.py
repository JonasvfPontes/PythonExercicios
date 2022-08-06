def fatorial(n=0, show=False):
    """
    → Calcula o faltorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for v in range(n, 0, -1):
        f *= v
        if show:
            print(f'{v}', end='')
            if v == 1:
                print(' = ', end='')
            else:
                print(' x ', end='')
    return f


print(fatorial(5, show=True))

