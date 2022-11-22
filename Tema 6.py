class Cerc:
    pi = 3.14
    culoare = 'verde'
    raza = '4'
    def descriere(self):
     print(f'Cercul are raza de', self.raza, 'si culoarea', self.culoare)

     def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def aria(self):
        return int(self.pi) * int(self.raza) ** 2

    def circumferinta(self):
      return 2 * int(self.pi) * int(self.raza)

    def diametru(self):
        return 2 * int(self.raza)

circle = Cerc()

print(f'Aria cercului este' , circle.aria())
print(f'Circumferinta cercului este' , circle.circumferinta())
print(f'Diametrul cercului este', circle.diametru())

circle_2 = Cerc()

print(f'Aria cercului este' , circle_2.aria())
print(f'Circumferinta cercului este', circle_2.circumferinta())
print(f'Diametrul cercului este' , circle_2.diametru())



print('.........................................................................')

class Dreptunghi:

    lungime = '5'
    latime = '6'
    culoare = 'portocaliu'

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        print(f'Dreptunghiul are lungimea de', self.lungime , ', latimea de', self.latime, 'si culoarea', self.culoare)
    def aria(self):
        return int(self.lungime) * int(self.latime)
    def perimetru(self):
        return  2*int(self.lungime) +2* int(self.latime)
    def culoare_noua(self,culoare_noua):
        self.culoare= culoare_noua

dreptunghiX=Dreptunghi('8', '5', 'albastru')
dreptunghiX.descriere()
print(dreptunghiX.aria())
print(dreptunghiX.perimetru())
dreptunghiX.culoare_noua('rosu')
dreptunghiX.descriere()

dreptunghiY=Dreptunghi('10', '20', 'portocaliu')
dreptunghiY.descriere()
print(dreptunghiY.aria())
print(dreptunghiY.perimetru())
dreptunghiY.culoare_noua('galben')
dreptunghiY.descriere()

print('...............................................................')

class Angajat:

    def __init__(self, Nume, Prenume, Salariu):
        self.Nume = Nume
        self.Prenume = Prenume
        self.Salariu = Salariu
    def descriere(self):
        print(f'Angajatul nostru de numeste',self.Nume,self.Prenume,'si are un salariu de', self.Salariu, 'lei')
    #def nume_complet(self):
     #   return self.Nume + ' ' + self.Prenume()
    def salariu_lunar(self):
        return int(self.Salariu)
    def salriu_anual(self):
        return int(12* int(self.salariu_lunar()))
    def crestere_salariala(self):
        return 10*int((self.Salariu))

angajatX = Angajat('Ionescu', 'Alina', '3500')
angajatX.descriere()
#print(angajatX.nume_complet())
print(angajatX.salariu_lunar())
print(angajatX.salriu_anual())
print(angajatX.crestere_salariala())

angajatY = Angajat('Georgescu', 'Ioana', '3000')
angajatY.descriere()
#print(angajatY.nume_complet())
print(angajatY.salariu_lunar())
print(angajatY.salriu_anual())
print(angajatY.crestere_salariala())


print('...................................................................')


class Cont:
    def __init__(self, Iban, titular_cont, sold):
        self.Iban = Iban
        self.titular_cont = titular_cont
        self.sold = sold


    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.Iban} suma de {self.sold}')
    def debitare_cont(self, suma):
        if self.sold >= suma:
            self.sold = int(self.sold) - int(suma)
            return self.sold
        else:
            return 'Ne pare rau! Fonduri insuficiente'
    def creditare_cont(self,suma):
        self.sold = int(self.sold) + int(suma)
        return self.sold
cont1 = Cont('Ro50', 'Ionescu Maria', '5000')
print(cont1.afisare_sold())
print(cont1.debitare_cont('5000'))
print(cont1.creditare_cont('3000'))

cont2 = Cont('RO24', 'Popescu David', '37000')
print(cont2.afisare_sold())
print(cont2.debitare_cont('5000'))
print(cont2.creditare_cont('3000'))

