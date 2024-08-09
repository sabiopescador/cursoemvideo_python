salario = float(input('Salário do funcionário R$: '))

if salario > 1250.00:
    aumento = salario + (salario * 10/100)
else:
    aumento = salario + (salario * 15/100)

print('Quem ganhava {} parará a ganhar {}'.format(salario, aumento))
