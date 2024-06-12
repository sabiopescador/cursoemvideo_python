n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('nota = {:.1f}'.format(m))
if m <= 6.0 and m > 5.5:
    print('recuperação')
elif m > 6.0:
    print('aprovado')
else:
    print('reprovado')
