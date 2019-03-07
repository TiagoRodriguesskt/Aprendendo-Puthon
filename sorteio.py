import random

n1 = str(input('1º alunoa(a): '))
n2 = str(input('2º alunoa(a): '))
n3 = str(input('3º alunoa(a): '))
n4 = str(input('4º alunoa(a): '))

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print('O alunoa(a) escolhido foi {}.'.format(escolhido))