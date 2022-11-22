class Persoane:   #definirea unei clase face prin keywordul Class scris cu majuscula
    nume = 'Roxana' #field, atribut, variabila locala / poate fi doar accesat nu si modificat
    sex = 'M'
    inaltime = '1,7'

    def prezentare(self): #functie locala (in interiorul clasei) care poate fi doar accesata. self este o referinta a instantei din clasa
        #este un obiect din clasa
        print(f'Ma numesc', self.nume, 'si am inaltimea de ', self.inaltime)

    #constructor

    def __init__(self, nume, sex, inaltime, varsta):
        self.nume = nume
        self.sex = sex
        self.inaltime = inaltime
        self.varsta = 32
persoana1 = Persoane('Maria', 'f', '1.72', '32') #initiallizarea unui obiect
print(persoana1.nume)   #folosirea unui atribut din clasa in obiectul definit
persoana1.prezentare() #apelarea unei metode din clasa prin intermediul obiectul persoana1

persoana2 = Persoane('Ovidiu', 'M', "1.84", '27')
print(persoana2.varsta)
persoana2.prezentare()

persoana2.nume = 'Maria'