#joc ghicit zarul
import random
dice_roll=random.randint(1,6)
b=int(input('Numarul ghicit de utilizator este:'))
while dice_roll!=b :
    if dice_roll>b:
        print('mai mare')
    else:
        print('mai mic')
    break
#else:
 #   print('ai ghicit numarul')


#avand stringul
lista=[0,1,2,3,4,5,6,7,8,9]
i=0
while i<len(lista):
    i=i+1
    if i%2==0:
            print(i)

    masini1 = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
    for x in range(len(masini1)):
        for y in range(1, len(masini1) - 1):
            masini1[y] = masini1[y].upper()
        print(masini1)


