times = 'Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Athletico PR', 'Internacional', 'Flamengo', 'Red Bull Bragantino', 'Santos', 'São Paulo', 'Ceará', 'Botafogo', 'Avaí', 'Goiás', 'Cuiabá-MT', 'Coritiba', 'América-MG', 'Atlético-GO', 'Fortaleza', 'Juventude'
print('\33[32m\nOs 5 primeiros colocados são: \33[m')
for c in range(0, 5):
    print(f'{c+1}º - {times[c]}')
print('\n\33[31mOs ultimos 4 são: \33[m')
for c in range(-4, 0, 1):
    print(times[c])
print('\n\33[34mPor ordem alfabética: \33[m')
for c in sorted(times):
    print(c)
print(f'\nO time \33[31mFlamengo\33[m está na {times.index("Flamengo") + 1}ª posição')
# Outra forma de mostrar o mesmo resultado é:
print(f'\33[36m\nOs cinco primeiros são {times[0:5]}')
print(f'Os 4 ultimos são {times[-4:]}')
