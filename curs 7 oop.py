import curs6
#mostenirea -- inheritence
class Dog():
    def __init__(self, rasa, talie, greutate, pedigree):
        self.rasa = rasa
        self.talie = talie
        self.greutate = greutate
        self.pedigree = pedigree

    def prezentare(self):
        print(f'Cainele meu este rasa, {self.rasa}, si are {self.greutate} kg')

caine1 = Dog('rottweiler', 'mare', 60, True)

class Shitzu(Dog):
    def __init__(self,talie, greutate, pedigree):
        self.rasa = 'Shitzu'
        self.talie = talie
        self.greutate = greutate
        self.pedigree = pedigree

    def mancare(self, tip):
        print(f'Rasa {self.rasa} mananca mancare de tipul Royal canin ')


caine2 = Shitzu('mica', 7, True)
caine2.prezentare()
caine2.mancare('pedigree')


#polimorfism
class Husky():
    def __init__(self, talie, greutate, pedigree):
        self.rasa = 'Husky'
        self.talie = talie
        self.greutate = greutate
        self.pedigree = pedigree

# abstractizare
    class Cat():
        def __init__(self, rasa, talie, greutate, pedigree):
            self.rasa = rasa
            self.talie = talie
            self.greutate = greutate
            self.pedigree = pedigree

    def mancare(self):
        pass


    def mancare(self):
        print(f'Rasa de caini {self.rasa} mananca mancare de tipul Purina')

caine3 = Husky('mare', 25, True)
caine3.mancare()

#incapsulare

class SaveInDataBase():
    __username = 'Tibi' #variabila privata ce nu poate fi accesata din afara clasei
    __pass = '12345'

    def __init__(self, tabela, username, __pass):
        self.__username = username
        self.__pass = __pass
        self.tabela = tabela

    def connection(self):
        print(f'Conexiunea la baza de date se face cu user {self.__username} si parola {self.__pass}')

    def SaveData(self, data):
        self.connection()
        print(f'Salveaza datele {data} in data base')

class SaveInMyDataBase():
    def sterge_user(self):
        self.username = ""


con1 = SaveInDataBase('persoane')
con1.__username = 'Ovidiu'
print(con1.__username)
con1.connection()

con2 = SaveInMyDataBase
con2.sterge_user()


#gettere si settere
class Sphinx():
    def __init__(self, __culoare):
        self.__culoare = __culoare

    @property
    def culoare(self):
        return self.__culoare

    @culoare.getter
    def culoare(self):
        return self.__culoare()
    @culoare.setter
    def culoare(self, __culoare):
        self.culoare = __culoare
        print(f'Culoarea este {self.__culoare}')

    @set
    def greutate(self, kg):
        self.__kg = kg
        print(f'pisica are greutatea de {self.kg}')


pisica = Sphinx('alba')
pisica.culoare()
pisica.culoare='gri'
pisica.culoare()