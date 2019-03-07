import random
print('Programa para ver a ordem do jogo: ')
q = int(input('Digite a quantidade: '))
lista = []
i = 1
while i <= q:
    alunos = input('Digite os números'+ str(i) +' :')
    lista.append(alunos)
    i += 1
print('A ordem dos números será:')
random.shuffle(lista)
print(lista)
exit('')