p = float(input('Me diz teu peso '))
h = float(input('Qual tua altura? '))
imc = p/(h*h)
print(f'IMC: {imc:.2f}')
if imc<18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <25:
    print('Tá show, \33[32mPrarabéns!\33[m')
elif imc >= 25 and imc < 30:
    print('Tá acima do peso!')
elif imc >= 30 and imc <40:
    print('Vai morrer se continuar assim... \33[44mFaça uma dieta!!!\33[m')
else:
    print('Xiii, deve ter morrido só de digitar, \33[41mOBESIDADE MÓRBIDA!\33[m')