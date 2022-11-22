import math
#TEMA 5
#functie care sa calculeze si sa returneze suma a doua numere
def func_suma(a,b):
    return a+b
print(func_suma(5,6))
def func_cu_2_params(a,b):
    func_cu_2_params(5,6)
    print(f'Suma numerelor este' + {a+b})


#functie care sa returneze true daca un numar este par, False pt impar
def func_return(numar):
    if numar%2 == 0:
        print('True')
    else:print("False")
x= func_return(6)

#functie care returneaza numarul total de caractere din numele tau complet

def lungime(nume):
    a = len(nume)
    return a
n = lungime('Krizbai MariaRoxana')
print('Numarul total de caractere este :' ,n )

#functie care returneaza aria dreptunghiului

def aria_dreptunchiului(a, b):
    aria = a*b
    return aria
x = aria_dreptunchiului(6, 12)
print(f'Aria dreptunghiului este:' , x)

#functie care returneaza aria cercului
def aria_cercului(r):
    arie_cerc=math.pi*r**2
    return arie_cerc
x = aria_cercului(6)
print(f'Aria cercului este:',x)

#functie care returneaza True daca un caracter x se gaseste intr-un string si False daca nu se gaseste
def chr_in_string (e,string):
    for i in range(len(string)):
        if e == string[i]:
            return True
        else:
            return False
        x = chr_in_string('e', 'elefant')
        print('Afirmatia este:', x)

#functie fara return, primeste un string ai printeaza pe ecran:
# Nr de caractere lowercase este x
#nr de caractere uppercase este y

#def funct_mea(string):
    x = 0
    y = 0
    for i in range(len(string)):
        if string[i].islower():
             x=x+1
        elif string[i].isupper():
             y=y+1
        else:
            pass
        funct_mea('Hello World')
#print('Numarul de caractere lowercase este:', x)
#print('Numarul de caractere uppercase este:', y)

#functie care primeste o lista de numere si returneaza doar numere pozitive


#functie care nu returneaza nimic,primeste doua numere si printeaza

def compaire(a, b):
  if a > b:
                print('Primul numart este mai mare decat al doilea')
  elif b > a:
                print('Al doilea numar este mai mare decat primul')
  else:
                print('Numerele sunt egale')

compaire(6, 7)


#functia care rpimeste un numar si un set de numere
#printeaza am adaugat numarul nou in set+returneaza true
#sau printeaza nu am adaugat numarul nou in set si returneaza false

def add_to_set(a,b):
    if a not in b:
        return True
        b.add(a)
        print('Am adaugat numarul:',a ,'in setul:', b)
    else:
        return False
    print('Nu am adaugat numarul:', a,'in setul:', b)
x=add_to_set(2,(1,3,4,5))
print('Afirmatia este:', x)