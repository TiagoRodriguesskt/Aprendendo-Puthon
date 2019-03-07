metros = float(input('Distancia em metros: '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('Em metros {}m corresponde a {:.0f}km, {:.0f}hm, {:.0f}dam, {}dm, {}cm, {}mm.'.format(metros, km, hm, dam, dm, cm, mm))
