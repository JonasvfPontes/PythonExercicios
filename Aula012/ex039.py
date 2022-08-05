import datetime
ano = int(input('Vc nasceu que ano? '))
idade = datetime.date.today().year - ano
if idade < 18:
    print(f'Vc tem {idade} anos, ainda vai se alistar')
elif idade == 18:
    print(f'Vc tem {idade} anos, está na hora de se alistar')
else:
    print(f'Vc tem {idade} anos, já passou do tempo de se alistar')
