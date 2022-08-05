nome = input('Qual é o seu nome? ')

if nome.capitalize() == 'Jonas':
    print('Nossa que nome lindo vc tem!')
elif nome.capitalize() =='Pedro' or nome.capitalize() == 'Maria' or nome.capitalize() == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome.lower() in 'ana claudia jessica juliana':
    print('Belo nome feminino!♥ ')
else:
    print('Seu nome é bem normal...')

print(f'Tenha um bom dia, {nome}!')
