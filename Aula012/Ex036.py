cs = float(input('Valor do imóvel: '))
sl = float(input('Renda mensal: '))
ano = int(input('Prazo em ano: '))
parcela = cs / (ano * 12)
if parcela / sl <= 0.3:
    print(f'Valor da percela é R${parcela:.2f}')
else:
    print('Sinto muito, não posso aprovar nessas condições.\nA parcel excede 30% da renda')
    print(f'\nParcela: \t\t\tR${parcela:.2f}\nRenda: \t\t\t\tR${sl:.2f}\nComprometimento:\033[0;31m \t{parcela/sl*100:.0f}%')
    