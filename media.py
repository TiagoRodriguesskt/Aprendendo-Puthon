nome = input('Digite seu nome: ')
print('Olá {}. Vamos calcular sua média escolar?'.format(nome))

n1 = float(input('Digite sua 1º nota! '))
n2 = float(input('Digite sua 2º nota! '))
n3 = float(input('Digite sua 3º nota! '))
n4 = float(input('Digite sua 4º nota! '))

result = (n1 + n2 + n3 + n4) / 4

#print('Sua média escolar é {:.2f}.'.format(result))

if result >= 6:
    print('PARABÉNS! Você foi Aprovado com a nota {}{}{}!'.format('\033[4;34m', result, '\033[m'))
elif result <= 5.9 and result >= 4:
    print('Infelizmente você ficou Recuperação com a nota {}{}{}!'.format('\033[4;33m', result, '\033[m'))
else:
    pass
    print('INFELIZMENTE você foi Reprovado com a nota {}{}{}!'.format('\033[4;31m', result, '\033[m'))



#PARA LEMBRA ONDE NÃO ESQUECER
'''if result >= 6:
   print ("você foi aprovado")
elif result <= 5.9 and result >= 4:
   print ("Você esta de recuperação")
elif result < 3.9:
   print ("Você esta reprovado")
else: #Observe que o else aqui não vai testar condições!
   print (n,"......")'''