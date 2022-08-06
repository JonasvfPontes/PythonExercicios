def voto(nascimento=0):
    import datetime
    vt = ' '
    idade = datetime.date.today().year - nascimento
    if idade < 16:
        vt = 'VOTO NEGADO'
        print(f'Com {idade} anos: {vt}')
    elif 16 <= idade < 18 or idade >= 65:
        vt = 'VOTO OPCIONAL'
        print(f'Com {idade} anos: {vt}')
    else:
        vt = 'VOTO OBRIGATÓRIO'
        print(f'Com {idade} anos: {vt}')



print('_' * 20)
nas = int(input('Em que ano você nasceu? '))
voto(nas)
