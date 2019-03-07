#ESSA É A FUNÇÃO MATEMÁTICA
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adiacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(hi))


'''
Pode soma ca hipotenusa usando uma biblioteca
import math
hi = math.hypot(ca, co)
'''