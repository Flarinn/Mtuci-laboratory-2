Height = 1.8
Weight = 40
Kolvo = 100000
Aktiv = 14
dlina = Height/4+0.37
distance = Kolvo*dlina/1000
skorost = distance/Aktiv
calor = 0.035*Weight+skorost**2/Height*0.029*Weight
print(f'Distance: {distance}, Calories: {calor}')
if distance < 2:
    print('Walk more')
elif distance > 4:
    print('very well')
else: print('not bad not good')
