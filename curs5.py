#functii
def prima_functie(): #declararea unei functii
    print('Aceasta este prima functie')   #corpul functiei

prima_functie()    #apelarea functiei


#functii cu parametrii
def functie_cu_parametrii(a):   #a este parametrul functiei
    print(f'parametrul este {a}')

functie_cu_parametrii(5)
functie_cu_parametrii([1,5,6])
functie_cu_parametrii('curs5')

def func_cu_params(a , b): #a si b sunt params deci trebuie tinut cond cand apelam functia sa ii pasam doua valori

    print(f'suma este {a + b}')



func_cu_params("2","5")
func_cu_params(2,5)

#functie cu multiplii parametrii
def func_cu_params_multiplii(*p): #* se refera la un numar indefinit de parametrii care pot fi pasati functiei in momentul apelarii
    print (f'unul din parametrii este {p[1]}')

func_cu_params_multiplii(2,4,6,'param') #param se vor stoca intr-un tuple

def functie_speciala(*masina):
    for i in masina:
        if masina == 'BMW':
            print(f'o vreau eu {i}')

functie_speciala("dacia", 'opel', 'BMW')

#functie cu parametrii pasati ca si dictionar
def functie_dict(**persoane):# se refera la un numar indefinit de parametrii care pot fi pasati functiei in momentul apelarii
    print(f'first name is: {persoane["prenume"]}')
    print(f'last name:{persoane["nume"]}')

functie_dict(nume='Kribai', prenume='Maria=Roxana')#params se vor stoca intr-un dictionar


#functie cu param default
def func_param_default(a, b = 10):#b este parametru default pentru ca este initializat la apelarea functiei
    print(f'suma este: {a+b}')
func_param_default(3, 5)# daca se paseaza doi parametrii cel de=al doilea il suprascrie pe primul


#functie cu parametrii de tip lista
def func_lista(lista):#parametru care trebuie pasat la apelareeste o lista din cauza corpului functiei in care se parcurge o lista
    for i in range(len(lista)):
        print (lista[i])

func_lista([1,4,7,9])



#functii cu return
def functie_return(a, b):
    return a + b   #aceasta functie va returna intotdeauna o valoare

print(functie_return(10, 12))  #se va printa ce va returna functia
c = functie_return(5,6)
print(c)


def func_retur(x, y):#functie cu return multiplu, functia se va termina cu primul return iar ce urmeaza nu va mai fi luat in considerare
    if x > y:
        return x
    else:
        return y
print(func_retur(4,6))


#exercitiu din tema
#functie care returneaza aria cercului
import math
def arie_cerc(r):
    aria = math.pi*r**2
    return aria
x=arie_cerc(4)
print(x)

#variabile globale si locale

a = 10 # a.variabila globala
def func_var(b): # b.parametru
    c = 15 #c. variabila locala
    return a + b + c
print(c)
print(func_var(4))