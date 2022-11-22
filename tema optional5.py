import math
from calendar import monthrange
def days_month (year, month):
    return monthrange(year, month)[1]
x = days_month(2016, 2)
print('Luna selectata are:', x ,'zile')

#functie calculator care sa returneze 4 valori,Suma, diferenta, inmultirea si impartirea a doua numere

def calculator (x, y):
    sum=x+y
    dif=x-y
    mul=x*y
    div=x/y
    return sum,dif,mul,div
a,b,c,d=calculator(7,4)
print('suma numerelor este:', a)
print('diferenta numerelor este:',b)
print('rezultatul inmultirii este:', c)
print('rezultatul impartirii este:', d)
