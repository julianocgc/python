n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s, m, d))
print('A divisão inteira é {} e a potência é {}'.format(di, e))