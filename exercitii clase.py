class vehicul:

    def __init__(self, cap_cilindrica,consum,  nr_locuri  ):
        self.cap_cilindrica = cap_cilindrica
        self.consum = consum
        self.nr_locuri = nr_locuri
    def prezentare(self):
        print(f'Masina noastra este un vehicul cu capacitate cilindrica {self.cap_cilindrica}, si un numar de locuri de {self.nr_locuri}')
class Masina(vehicul):

    def __init__(self, model):
        self.model = model
vehicul = vehicul('2.0 TDI', '9', '5')
vehicul.prezentare()

masina = Masina('Dacia')

masina.consum = '5,6'
print(masina.consum)

print('..............................................................................................................')


class Cerc:
    pi = 3,14
    def __init__(self, raza):
     self.raza = raza

     def aria(self):
         return int(self.pi)* int(self.raza)**2


cerc = Cerc('6')
print(cerc.aria())