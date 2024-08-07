print('vamos ver quais métodos você usaria para saber o ano bissexto: ')

ano = int(input('ANO: '))

if ano % 4 == 0:
    print('O ANO {} É BISSEXTO! :D'.format(ano))
else:
    print('O ANO {} NÃO É BISSEXTO :F'.format(ano))
