produto = float(input('Qual o preço do prduto? R$ '))
novo = produto * 5
preco = novo / 100
resul = produto - preco
print('O produto que custava R${:.2f}, tem desconto de 5%.\nSeu novo preço é R${:.2f}.\nVocê ganhou desconto de R${:.2f}.'.format(produto, resul, preco))