height = 1.8
weight = 40
kolvo = 100000
aktiv = 14
dlina = height/4+0.37
distance = kolvo*dlina
skorost = distance/aktiv
calor = 0.035*weight+skorost**2/height*0.029*weight
print(f'Distance: {distance}, Calories: {calor}')
