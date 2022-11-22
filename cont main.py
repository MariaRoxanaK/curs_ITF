from oop.cont_bancar import Cont_bancar

cont1 = Cont_bancar('Roxi K', 'RO001')
cont2 = Cont_bancar('Szabi K', 'RO002')

cont1.activareCont(0000)
cont2.activareCont(2222)
cont2.activareCont(0000)

cont1.alimentareCont(4000)
cont2.alimentareCont(4000)
cont2.alimentareCont(200)

cont1.interogareSold()
cont2.interogareSold()

cont1.plataCard(1000)
cont2.plataCard(2500)
cont2.plataCard((25))