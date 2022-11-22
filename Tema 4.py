#avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in range(len(masini)):
    print('Masina mea preferata este:' + masini[x])
#acelasi lucru cu un for each
print('for each')
for masini in masini:
    print('Masina mea preferata este ' + masini)
#acelasi lucru cu un while
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
i = 0
while i < len(masini):
    print('Masina mea preferata este ' + (masini[i]))
    i += 1

#2aceeasi lista folositi un for
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masini in masini:
    print('Masina mea preferata este '  +  (masini))
#prima si ultima litera din string in lowercase
masini1 = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in range(len(masini1)):
    for y in range(1,len(masini1)-1):
          masini1[y]=masini1[y].upper()
    print(masini1)


#exercitiul3
masini1 = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
print('for each')
for i in masini1:
    if i == 'Mercedes':
        print('Am gasit masina cautata ')
        break
else:print(f'Am gasit masina   {i}.Mai cautam.')
#exercitiul4
masini1 = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in masini1:
    if (x == 'Lastun' or  x =='Trabant'):
        continue
else:print('S-ar putea sa va placa masina' +  x  )

#modernizati parcul de masini
masini_vechi=[]
for i in range(len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lastun':
      masini_vechi.append(masini[i])
    masini[i] == 'Tesla'
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')
#6avand dict
pret_masini = {
    'Dacia':6800,
    'Lastun':500,
    'Opel':1100,
    'Audi':19000,
    'BMW':23000
}
#vine un client cu un buget de 15000 euro
#prezentati doar masinile care se incadreaza in acest buget
for x in pret_masini:
    if pret_masini[x]<=15000:
        print(x)
    for x in pret_masini.items():
        print(x)
    for x in pret_masini:
     if pret_masini[x]<= 15000:

         print("pentru un buget sub 15000 puteti achiziona masina " + x)


#7avand lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0,-4, 3]
#afisati de cate ori apare 3
i=0
for numar in numere:
    if numar==3:
        i=i+1
        print(i)

#8calculati si afisati suma numerelor
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0,-4, 3]
suma = 0
for x in numere:
    suma = suma + x
    print(suma)
#9 afisati cel mai mare numar
max=sorted(numere)[-1]
print(max)

#din pozitive in negative
numere_negative=[]
for x in range (len(numere)):
    if numere[x]>0:
        numere[x]=-numere[x]
        numere_negative.append(numere[x])
        print(numere_negative)
    else:print(numere_negative)






