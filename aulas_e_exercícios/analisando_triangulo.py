print('ANALISANDO TRIÂNGULOS')
seg_1 = float(input('Primeiro segmento: '))
seg_2 = float(input('Segundo Segmento: '))
seg_3 = float(input('Terceiro Segmento: '))

if seg_1 < seg_2 + seg_3 and seg_2 < seg_1+ seg_3 and seg_3 < seg_2 + seg_1:
    print('Esses Elementos podem formar um triângulo')
else:
    print('Não podem formar triângulos')
print('FIM DO MUNDO 1! :D')