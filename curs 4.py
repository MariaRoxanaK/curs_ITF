#cicluri repetitive
#while
i = 1
while i < 4:
    print(i)
    i+=1
x = 10
y = 5
#while si else
while x > 0 and y < 8:
    print(x+y)
    x-=2
    y-=1
else:
    print("valorile lui x si y sunt" + str(x) + str(y))

#whil- break
#x = 10
#while x > 0:
#    print (x)
    if x == 4:
       # break
        x-=2
        y-=1
#while - continue
print("continue")
y = 8
while y > 4:
    y-=1
    continue

#for
for i in range(4):
    print (i)
else:
    print(i)

#for each
print("for each")
logo = "apple"
for x in logo:
    print(x)
firme = ['kfc', 'mcdonalds', 'subway']
for x in firme:
    print(x)

dict = {
    "masina" : "dacia" ,
    "casa" : "mare"
}
for x in dict.keys():
    print(dict[x])
    print(x)
#[x]-cheia
#x-dictionarul

#for break
print("for - break")
dict = {
    "masina" : "dacia" ,
    "casa" : "mare"
}
for x in dict:
    if dict[x] ==  "mare":
        break
        print(x)
print("for - continue")
firme = ['kfc', 'mac', 'subway']
#for x in dict:
    #if dict[x]

#exercitiu
lista = ['mar', 'para' , 'cirese' , 'portocale']
#for x in lista:
    #lista.pop(1)
    #print(lista)

for x in range(len(lista))  :
    print(x)

for x in range(len(lista)):
    print(lista[x])