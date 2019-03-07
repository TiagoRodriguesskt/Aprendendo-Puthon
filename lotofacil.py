import random

lista = [1, 25]
contador = 1

while contador < 15:
    palpite = random.randint(1, 25)
    if palpite not in lista:
        contador += 1
        lista.append(palpite)
    else:
        pass

lista.sort()

print('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},{}'.format
      (lista[1], lista[2], lista[3], lista[4], lista[5], lista[6],
       lista[7], lista[8], lista[9], lista[10], lista[11], lista[12],
       lista[13], lista[14], lista[15]))