dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km o carro andou? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(pago))