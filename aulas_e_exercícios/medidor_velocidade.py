n = float(input('Velocidade do carro [km/h]: '))

multa = n-80

if n > 80:
    print('você foi multado em [{}] Reais!'.format(multa*7))
else:
    print('Tenha uma boa viagem!')