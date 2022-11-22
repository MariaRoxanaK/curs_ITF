'''structuri de date'''
#listele in python pot sa cuprinda elemente de tipuri diferite
#au dimensiune dinamica

fructe = ['mar', 'banane', 'portocala', 3, True, 3 ]

#afisam o lista
print(fructe)

#accesam un element in functie de index

print(fructe[2])# indexul incepe numaratoarea de la0 deci 0 va si mar, 1 va fi banane,2 vor fi portocale

#adaugam un nou element

fructe.append('rosie')
print(fructe)

#suprascriem un element

fructe[0] = 'para'
print(fructe)

#aflam dimensiunea
print(len(fructe))

#ne da ultimul element (scoate si ne returneaza ultimul element)

last = fructe.pop()
print('ultimul element:',last)
print('lista:', fructe)

#de cate ori apare un element

print(fructe.count(3))

#extindem lista
fructe_exotice=['ananas' , 'kiwi', 'mango']
fructe.extend(fructe_exotice)
print(fructe)


'''map = dict'''

note_elevi = {'Gigel': 10, 'Costel': 9, 'Oana': 10}

#adaugam un elev nou
note_elevi['Sebi']= 7

#printam dictul
print(note_elevi)

#aflam elemente dinauntru-aflam nota
print(note_elevi['Gigel'])
print(note_elevi.get('Gigel'))

#actualizam valori
note_elevi['Costel']= 10
print(note_elevi)

#aflam dimensiunea
print(len(note_elevi))

#stergem valori
note_elevi.pop('Gigel')
print(note_elevi)