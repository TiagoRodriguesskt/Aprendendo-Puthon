salario = float(input('Qual o valor do seu salário? '))
novo = salario + (salario * 15 /100)
#sal = novo / 100
#resul = novo + sal
print('Seu salário era R${}, você ganhou aumento de 15%, foi para R${}.'.format(salario, novo))