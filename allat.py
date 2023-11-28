class Allat:
    def __init__(self, nev):
        self.nev = nev

    def mianeved(self):
        print(f"{self.nev}")


class Kutya(Allat):
    def hangotad(self):
        print(f"Vau")


class Negylabu:
    LABAK_SZAMA = 4

    def __init__(self):
        print('Negylabu')


class Macska(Allat, Negylabu):

    def __init__(self, nev, eletkor):
        Allat.__init__(self, nev)
        Negylabu.__init__(self)
        super().__init__(nev)
        self.eletkor = eletkor


bodri = Kutya('Bodri')
bodri.mianeved()

tom = Macska('Tom', 2)
tom.mianeved()

