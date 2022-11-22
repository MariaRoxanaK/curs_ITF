#cum functioneaza "if else"
'''if reprezinta conditia iar else reprezinta o alta varianta ( if conditia se verifica atunci se executa codul, else
se va executa cealalta varianta
'''


#verifica si afiseaza daca x este un numar natural sau nu

x = 2
numere_naturale = [0,1 ,2,3,4,5,6]

if x >= 0:
    print('2 este numar natural')
else:
    print('2 nu este numar natural')

#verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

if x > 0 :
    print(' 2 este numar pozitiv')
elif x < 0:
    print('2 este numar negativ')
else:
     print('2 este numar neutru')

#verifica si afiseaza daca x este intre -2 si 13

list=[-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13]
x = 2
if x in list:
    print("exista")
else:
    print("nu exista")
#verifica si afiseaza daca diferenta dintre x si y este mai mica decat 5

x = 2
y = 0
if x - y < 5:
    print('diferenta este mai mica decat 5')
elif x - y == 5:
    print('diferenta este egala cu 5')
else:print('diferenta este mai mare decat 5')

#verifica daca x Nu este intre 5 si 27(a se folosi 'not')

x = 2
list=[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
if x not in list:
        print('nu exista in lista')

#x si y (int).verifica si afiseaza daca sunt egale, daca nu afiseaza care dintre ele este mai mare

x = 9
y = 8

if x == y:
    print('sunt egale')
elif x > y:
    print('x este mai mare decat y')

#x, y si z sunt laturile unui triunghi.afiseaza daca triunghiul este isoscel, echilateral sau oarecare

x = 7
y = 7
z = 7

if x == y == z:
    print('triunghiul este echilateral')
elif x == y != z:
    print('triunghiul este isoscel')
else:print('triunghiul este oarecare')

# exemplul2
x = 7
y = 7
z = 8

if x == y == z:
    print('triunghiul este echilateral')
elif x == y != z:
    print('triunghiul este isoscel')
else:print('triunghiul este oarecare')

#citeste o litera de la tastatura
'''verifica daca este sau nu vocala'''

ch = ('r')
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print('litera este vocala')
else:print('litera este consoana')

#transforma si printeaza literele din sistem romanesc





#optionale
#verifica daca x are minim 4 cifre

x = 257
def uniq4(num):return len(set(list(str(num)))) == 4
if x == 4:
    print('are 4 cifre')
else:print('x are trei cifre')

#verifica daca x are fix 6 cifre

x = 123456
def ungiq6(num):return len(set(list(str(num)))) == 6
if x == 5:
    print('are doar 5 cifre')
else:print('are fix 6 cifre')

#verifica daca x este par sau impar

x = 12
if x % 2 == 0:
    print("numarul este par")
else:print("numarul este impar")

#ex 2

x = 7
if x%2 == 0:
    print('numarul este par')
else:print('numarul este impar')

#x,y,z = int; afiseaza care este cel mai mare
x = 1
y = 3
z = 5
if z >= y:
    print('Z este numarul mai mare')
else:print('Y este numarul mai mare')
if z >= x:
    print('Z este numarul mai mare')
else:print('Y este numarul mai mare')

#x , y , z sunt unghiurile unui triunghi.verifica si afiseaza daca triunghiul este valid sau nu

x = float(50)
y = float(80)
z = float(50)

if x+ y+ z == 180:
    print('triunghiul este valid')
else:
    print('triunghiul nu este valid')









