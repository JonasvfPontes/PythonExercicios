import datetime
funcionario = {}
while True: #Nem precisaria desse while
    funcionario["Nome"] = input('Nome: ').strip().capitalize()
    funcionario["Nascimento"] = int(input('Ano de nascimento: '))
    funcionario["Cart trab"] = int(input('Carteira de Trabalho: (0 = não tem) '))
    if funcionario["Cart trab"] == 0:
        break
    funcionario["Ano contrato"] = int(input('Ano de contratação: '))
    funcionario["Salário"] = 'R$' + input('Salário: R$')
    funcionario["idade"] = datetime.date.today().year - funcionario["Nascimento"]
    funcionario["Aposentadoria"] = (funcionario["Ano contrato"] + 50) - datetime.date.today().year
    break
for v, i in funcionario.items():
    print(f'{v} tem o valor de {i}')
