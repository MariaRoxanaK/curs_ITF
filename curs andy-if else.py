'''capitol nou IF ELSE'''
piesa_faina = True
print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonez piesa')
print('oprim radio')

print('.....................................................')

piesa_faina = False
print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonez piesa')
print('oprim radio')


#if else -statement
#daca nr este par printam acest lucru
#altfel printam impar

nr = 4

#ce inseamna par? se imparte exact la 2
#ce inseamna ca se imparte exact la doi? ne da restul 0

if nr % 2 == 0:
    print('numarul este par')
else:
    print( 'impar')


nr = 5

#ce inseamna par? se imparte exact la 2
#ce inseamna ca se imparte exact la doi? ne da restul 0

if nr % 2 == 0:
    print('numarul este par')
else:
    print( 'impar')

print('..............................................................')



#este un numar pozitiv?
if (nr>0):
    print('pozitiv')
else:print('nr nu este pozitiv')


print('...............................................')
#if, else if, else
#cum ne saluta robotelul in functie de ora
#luam date de la tastatura
#ne asiguram ca sunt transformate din string in int
#   ctrl+ /

# ora = int(input('Introdu ora'))
# if ora < 0:
#     print('ora negativa.ora invalida')
# elif ora <= 11:
#     print(' buna dimineata')
# elif ora <= 18:
#     print('Buna ziua')
# elif ora <= 21:
#     print('buna seara')
# elif ora <= 24:
#     print('Noapte buna')
# else:
#     print('ora mai mare decat 24.ora invalida')

print('..............................................')
#xercitiu: masina in miscare sau in stationare

# km_ora = int(input('cati km pe ora are masina?'))
# if km_ora <= 0:
#     print('Masina este in stationare')
# elif km_ora <= 50:
#     print('Masina circula in localitate')
# elif km_ora <= 80:
#     print('Masina este in afara localitatii')
# elif km_ora <= 130:
#     print('Masina circula pe autostrada')
# else:
#     print('Masina este defapt avion')

print('.....................................')

#exercitiu robot telefonic

optiunea = int(input('apasa tasta'))
if optiunea == 0:
    print('meniu anterior')
if optiunea == 1:
    print('pentru limba roamana, apasa tasta 1')
elif optiunea == 2:
    print('for english press 2')
else:
    print('optiunea selectata nu exista.va rugam reveniti')