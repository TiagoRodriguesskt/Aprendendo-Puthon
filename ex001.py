#Digitando seu nome, calculadora básica com raiz quadrada

#Aqui é nome
nome = input('Digite seu nome: ')

#Os dois números
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número:'))

#Sucessor e antecessor de n1
s = n1 + 1
a = n1 - 1
#Sucessor e antecessor de n2
suc = n2 + 1
ant = n2 - 1

#Agora o dobro, triplo de n1
dobro = n1 * 2
triplo = n1 * 3

#Agora o dobro, triplo de n2
dob = n2 * 2
tri = n2 * 3

#calculando os dois números
mult = n1 * n2
divi = n1 / n2
soma = n1 + n2
subt = n1 - n2
raiz = ((n1 + n2) ** (1/2))

#Imprimindo os resultados
print('Muito prazer, {}!\n'.format(nome))
print('Aqui estão seus resultados!!!\n')
print('A multiplicação de seu número foi, {}.'.format(mult))
print('A divisão de seu número foi, {:.2f}.'.format(divi))
print('A soma de seu número foi, {}.'.format(soma))
print('A subtração de seu número foi, {}.'.format(subt))
print('A raiz dos dois números somados foi, {:.2f}.'.format(raiz))
print('\nO sucesso e antecessor de 1º número.')
print('O sucessor de {} é {}.'.format(n1, s))
print('O antecessor de {} é {}.'.format(n1, a))
print('\nO sucessor e antecessor de 2º número.')
print('O sucesso de {} é {}.'.format(n2, suc))
print('O antecessor de {} é {}.'.format(n2, ant))
print('\nO dobro e o triplo do 1º número.')
print('O dobro de {} número é {}.'.format(n1,dobro))
print('O triplo do {} número é {}.'.format(n1, triplo))
print('\nO dobro e o triplo do 2º número.')
print('O dobro de {} número é {}.'.format(n2, dob))
print('O triplo do {} número é {}.'.format(n2, tri))