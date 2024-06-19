import random

n = int(input('Digite um número inteiro: '))

rd = random.randint(0,5)

if n == rd:
    print('Você Acertou!')
else:
    print('Você errou...o número correto foi [{}]'.format(rd))
    
