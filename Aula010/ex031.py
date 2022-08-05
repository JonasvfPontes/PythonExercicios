km = float(input('Distancia da viagem: '))
print('\n--- TABELA DE PREÇOS ---\nViagens até 200Km = R$ 0,50/Km\nAcima de 200Km    = R$0,45/Km\n----------')
if km > 200:
    x = 0.45
else:
    x = 0.5
print(f'Sua passagem deu R${km*x:.2f}')
