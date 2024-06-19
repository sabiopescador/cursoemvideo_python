n = float(input('Qual a distância em km? '))
if n <= 200:
    passagem  = n/2
    print('Valor da taxa: [{}] Reais'.format(passagem))
else:
    passagem = n*0.45
    print('Valor da taxa: [{}] Reais'.format(passagem))

