cidade = input('Nome da sua cidade ').strip()
dividido = cidade.split()
print('Cidade começa com "Santo"?: {}'.format('santo' in dividido[0]))