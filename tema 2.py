#tema2

#1variabila este o zona de memorie care stocheaza valori(cutiuta)


#declaram si initializam variabile
#variabila_string
titlu_carte = 'Secretele succesului'
print(titlu_carte)

#variabila int
numarul_de_pagini = 243
print(numarul_de_pagini)

#variabila float
pretul_cartii = 39.99
print(pretul_cartii)
print(pretul_cartii)

#variabila bool
autorul_cartii_Dale_Carnegie = True
print(autorul_cartii_Dale_Carnegie)

print(f'Am achizitionat cartea {titlu_carte} cu pretul de {pretul_cartii}. Aceasta are {numarul_de_pagini} pagini'
      f' si autorul este{autorul_cartii_Dale_Carnegie} Dale Carnegie.')

#functia type
print(type(titlu_carte))
print(type(pretul_cartii))
print(type(numarul_de_pagini))
print(type(autorul_cartii_Dale_Carnegie))

#rotunjiti float-ul
print(round(pretul_cartii))
#overwrite
pretul_cartii = 40
print(pretul_cartii)
print(type(pretul_cartii))

#folosit print pentru a printa in consola 4 propozitii cu cele 4 variabile

print(f'Am achizitionat de la librarie cartea {titlu_carte}.')
print(f'Aceasta carte a costat{pretul_cartii}.')
print(f'Cartea are {numarul_de_pagini } de pagini.')
print(f'Autorul cartii este Dale Carnegie.{autorul_cartii_Dale_Carnegie}.')

#aflam dimensiunea unui string
numele = input('Krizbai')
prenumele = input('Maria Roxana')

print('nume'+ 'prenumele')

print(len(numele+prenumele))


#7 citim de la tastatura lungimea si latimea

lungime = 22
latime = 35
print(lungime)
print(latime)

print(f'Aria dreptunghiului este {lungime*latime}')

#avand stringul
str1 = 'Coral is either the stupidest animal in the world or the smartest rock'
substr = 'the'
count1 = str1.count(substr)
print(count1)

a = 'Coral is either the stupidest animal in the world or the smartest rock'
print(a.count('the'))

txt = 'THE'
x = txt.upper()
print(x.upper())
original = 'Coral is the stupidest animal in the world or the smartest rock'
replace = original.replace('the' , 'THE')
print(replace)

a = 'Coral is the stupidest animal or the smartest rock'
b = a.isnumeric()
print(b)