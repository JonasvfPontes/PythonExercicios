import datetime
ano = int(input('Tu nasceu em que ano? '))
idade = datetime.date.today().year - ano
if idade <= 9:
    print('vc é MIRIM')
elif idade <= 14:
    print('Vc é INFANTIL')
elif idade <= 19:
    print('Vc é JUNIOR')
elif idade <= 20:
    print('Vc é SÊNIOR')
else:
    print('Vc é MASTER')