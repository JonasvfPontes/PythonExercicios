def voto(nascimento=0):
    from datetime import date
    vt = ' '
    idade = date.today().year - nascimento
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print(voto(int(input('Em que ano você nasceu? '))))
