#declara o lista de note muzicale
lista_mea = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(lista_mea)
#inverseaza ordinea folosind slicing
print((lista_mea[::-1]))
#overwright
lista_mea = ['do', 'si', 'la', 'sol', 'fa', 'mi', 're', 'do']
print(lista_mea)
#pe aceasta lista foloseste o metoda care banuiesti ca face acelasi lucru
lista_mea.reverse()
print(lista_mea)
#de cate ori apare do
print(lista_mea.count("do"))
#avand doua liste, gasiti 2 metode sa le uniti
#varianta1
lista_mea1 = [3,1,0,2]
lista_mea2 = [6, 5, 4]
lista_mea3 = lista_mea1 + lista_mea2
print(lista_mea3)
#varianta2nu este buna
lista_mea1.append(lista_mea2)
print(lista_mea1)
#sortati si afisati lista generata la exercitiul anterior
lista_mea.sort()
print(lista_mea3)
#stergeti numarul 0 folosind o functie
x = lista_mea3.remove(0)
print(lista_mea3)
#folositi un if si verificati daca lista este goala sau nu
lista_mea3 = [3, 1, 0, 2, 6, 5, 4]
lista_goala = []
if lista_mea3 != lista_goala:
    print("lista mea nu este goala")
else:print("lista este goala")
#folositi o functie care sa stearga lista de la ex 3
lista_mea3.clear()
print(lista_mea3)
#copy paste ex 5.acum ar trebui sa afiseze ca e goala
if lista_mea3 != lista_goala:
    print("lista mea nu este goala")
else:print("lista este goala")
#avand dictionarul{} folositi o functie care sa afiseze elevii
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel' : 5 }
print(dict1)
elevii = dict1.keys()
print(dict1.keys())
#printati cei 3 elevi si notele
my_sets = {8 , 10 ,5}
for x in my_sets:
    print('Ana a luat nota', dict1['Ana'])
print('Gigel a luat nota' , dict1['Gigel'])
print('Dorel a luat nota', dict1['Dorel'])
#Dorel a facut contestatie/ overwright
dict1['Dorel'] = 6
print(dict1)
#gigel se transfera din clasa
dict1.pop('Gigel')
print(dict1)
#vine coleg nou Ionica cu nota 9
dict1['Ionica'] = 9
print(dict1)
#zilele saptamanii
zile_sapt = 'sambata', 'duminica'
zile_weekend = 'sambata', 'duminica'
#adaugati luni
zile_sapt = ('sambata' , 'duminica')
zile_sapt2 = zile_sapt + ('luni', )
print(zile_sapt2)
#folositi un if si verificati daca
if zile_weekend == zile_sapt:
    print('weekendul este un subset al zilelor saptamanii')
else:print('weekendul nu este un subset al zilelor saptamanii')


