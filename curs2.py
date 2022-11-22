#opeartori de atribuire
x = 10
x += 5 #x=x+5
x -= 7 #x=x-7
x *= 2 #x=x*2
x /= 3 #x=x/3
x %=4 #x=x%4
x //= 2 #x=x//la puterea a 2 a (x**)

#operatori aritmetici
x = 5
y = 2
z = x ** y
print((z))

z = x % y
print(z)

#operatori de comparare

x == y #egal
x != y #diferit
x > y  #mai mare
x < y #mai mic
x >= y #mai mare sau egal
x <= y #mai mic sau egal

#operatori logici

x and y #si (daca x e true si y e fals)
x or y #ori
not x #negatie

#if statement
a = 20
b = 30
if  b > a:
    print("succes")

if b < a:
    print("succes")

if (b + a) == 50 and b > a:
   print("succes")
else:
    print("mai incearca")
if (b + a) < 50 and b > a:
    print("succes")

#if elseif statement

a = 5
b = 9



if b > a:
    print("succes")
elif b == a:
    print("aici e bine")
elif a > b:
    c = a+b
    print(type(c))
else:
    print("iesire")

#if else in oneline

#nested if

if a == b:
    if a+b == 14:
        print ("succes3")
    else:
        print ("iesire")

if a>b:
    pass
elif b==a:
    print(a)
else:
    print(b)


