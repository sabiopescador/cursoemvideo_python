import colorpyteo
print(colorpyteo.colorful_text('MAIOR E MENOR VALOR', font='digital', color='green'))

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))  

maior = a
menor = a

if b > maior:
    maior = b
if c > maior:
    maior = c

if b < menor:
    menor = b
if c < menor:
    menor = c

print('\nO menor valor digitado foi: \033[31m{}\033[m'.format(menor))
print('O MAIOR velor digitado foi: \033[32m{}\033[m\n'.format(maior))

