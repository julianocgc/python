casa = float(input('Qual é o valor da casa? '))
salário = float(input('Qual é o seu salário atual? '))
anos = int(input('A casa será financiada em quantos anos? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos,'.format(casa, anos),end='')
print(' a prestação será de R$ {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo CONCEDIDO!!!')
else:
    print('Empréstimo NEGADO!')
