# ler se o ano é bissexto
from datetime import date

'''Chama-se ano bissexto o ano ao qual é acrescentado um
dia extra, ficando com 366 dias, um dia a mais do que
os anos normais de 365 dias, ocorrendo a cada quatro anos
(exceto anos múltiplos de 100 que não são múltiplos de 400)'''

ano = int(input('Digite um ano, se quiser analisar ano atual digite 0 '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    x = 'É'
else:
    x ='NÃO É'
print(f'O ano {ano} {x} BISSEXTO')
