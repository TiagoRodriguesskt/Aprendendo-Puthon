'''velocidade = float(input('Qual a velocidade do carro? '))
velocidadeLimite = 80 #Velocidade limite da via
multaExcedente = 7 #Valor da Multa cobrada por excedente

if velocidade > velocidadeLimite:
    print('Seu TRANSGRESSOR.')
    print('Sua multa será de R$ {:.2f}.'.format((velocidade - velocidadeLimite) * multaExcedente))
else:
    print('Muito bem! Continue dirigindo com prudência.')'''

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite que é de 80Km.')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia!')
