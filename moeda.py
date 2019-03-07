#converso de moeda

real = float(input('Quantos de dinheiro você tem na carteira? R$'))
dolar = real / 3.76
euro  = real / 4.24
print('Você tem em R${}, que dar para compra US${:.2f}.'.format(real, dolar))
print('Você tem em R${}, que dar para compra €${:.2f}.'.format(real, euro))

