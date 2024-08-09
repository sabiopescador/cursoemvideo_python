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

print('O menor valor digitado foi: {}'.format(menor))
print('O MAIOR velor digitado foi: {}'.format(maior))

