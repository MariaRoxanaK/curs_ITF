#liste
list_mea = ["masina", "casa", True, 22, 67.6]

#operatii cu liste
#index
print (list_mea[0])
print((list_mea[1:3]))#slicing
print((list_mea[1::2]))
print((list_mea[:3]))
print(list_mea[-3:-1])


if True in list_mea:
    print("succes")
if 27 in list_mea:
    print("valoarea este in lista")

#append
list_mea.append("4")
print(list_mea)

#inssert
list_mea.insert(1, "mancare")
print(list_mea)

#extend
lista_2 = ["masline", 4]
list_mea.extend(lista_2)
print(list_mea)

#remove
list_mea.remove('masina')
print(list_mea)

#pop
list_mea.pop(1)
print(list_mea)
list_mea.pop()
print(list_mea)

#del
#del lista_2
print(lista_2)

#clear
#lista_mea.clear()
#print(lista_mea)

#sort
#list_mea.sort()
print(list_mea)

#copy
lista_ta = list_mea.copy()
print(lista_ta)

#list
#lista_2 = list(list_mea)
#print(lista_2)

#concatenare
lista_4 = lista_ta + lista_2
print(lista_4)

#type
print(type(list_mea))

#len
print(len((lista_2)))

#count
print(lista_2.count(('b')))

#change elements in list(schimba doua elemente din lista, elemente precizate de noi)
list_mea[1] = [10,3,5]
list_mea[1:3] = ["da" , "nu"]
print(list_mea)

#loop list
for x in list_mea:
    print(x)



#dictionar
dict_meu = {"masina": "BMW",
            "automata": True
}
print(dict_meu)

#index bazate pe key
valoare = dict_meu["masina"]
print(valoare)

print(dict_meu.get("automata"))
#aflam keys din dictionar
print(dict_meu.keys())

#adaugare de elemente noi
dict_meu["culoare"] = "verde"
print(dict_meu)
#suprascriere
dict_meu["masina"] = "dacia"
print(dict_meu)

#items()
a = dict_meu.items()
print(a)
print(type(a))
print(type(dict_meu))


#check if key or values in dict
if "culoare"in dict_meu:
    print("avem culoarea" + dict_meu["culoare"])
elif "dacia " in dict_meu.values():
    print("avem dacia")

#remove items
#dict_meu.pop("culoare")
#print(dict_meu)
#del dict_meu["automata"]
#print(dict_meu)
#dict_meu.clear()
#print(dict_meu)

#copiere de dict

dict_nou = dict_meu.copy()
dict_extra_nou = dict(dict_meu)
print(dict_nou)
print(dict_extra_nou)

#nested dict
dict_tau = {
    "copil1": {
        "nume": "natalia",
        "ani": 1
    },
    "copil2": {
        "nume": "sofia",
        "ani": 3
    }
}

#len
print(len(dict_tau))

#tuples
my_tuple = ("dacia", "bmw", 2)
print(my_tuple[1])
#my_tuple[1] = ["renault"]= valoarea nu suporta alt assignement
x = list(my_tuple)
#workaround pentru a adauga element nou
x[1] = "renault"
my_tuple = tuple(x)
print(my_tuple)
tuple_nou = ("bmw",4)
tuple_nou = my_tuple + tuple_nou
print(tuple_nou)

#len
print(len(tuple_nou))

#sets
my_sets = "masina", "casa", 12
#accesare valori
for x in my_sets:
    print(x)
#my_sets.__add__(False)
#print(my_sets)

#stergere element
#my_sets.remove("casa")
#print(my_sets)

#my_sets.pop()
print(my_sets)