class Cont_bancar:
    # constructorul
    def __init__(self, titularCont, Iban):
        # atribute, fields
        self.titularCont = titularCont
        self.Iban = Iban
        self.sold = 0
        self.activ =True
        self.pin = 0000
        self.incercari_activare = 0

    def interogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'contul {self.Iban}')
        print(f'Soldul contului {self.sold}')
        print(f'Contul este activ {self.activ}')
        print(f'numarul de incercari {self.incercari_activare}')

    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print('Card activat')
            self.activ = False
        else:
            print('Pin gresit')
            self.incercari_activare = self.incercari_activare + 1
            self.incercari_activare += 1

    def alimentareCont(self, suma):
        self.salut()
        self.sold += suma
        print(f'Ati alimentat {suma}')
        print(f'Aveti in cont {suma}')

    def plataCard(self, suma):
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit {suma}')
            print(f'Aveti in cont {self.sold}')
        else:
            print('Fonduri insuficiente')

    def salut(self):
        print(f'Buna {self.titularCont}')
