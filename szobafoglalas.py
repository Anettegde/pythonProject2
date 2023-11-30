class Szoba:

    def __init__(self,ar,szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):

        def __init__(self,ear,eszobaszam):
            self.ear = ear
            self.eszobaszam = eszobaszam

        def __str__(self):
            return f"Egyágyasszoba szám: {self.eszobaszam}, Ára: {self.ear}"


class KetagyasSzoba(Szoba):

    def __init__(self, kar, kszobaszam):
        self.kar = kar
        self.kszobaszam = kszobaszam

    def __str__(self):
        return f"Kétágyasszoba szám: {self.kszobaszam}, Ára: {self.kar}"


class Foglalas:
    pass


class Szalloda:

    def __init__(self, nev):
        self.nev = nev

    def __str__(self):
       return f"A szálloda neve: {self.nev}"

    def szobaadat(self):
        self.addszoba(EgyagyasSzoba(25000,25))
        self.addszoba(KetagyasSzoba(55000,55))


def foglal(szalloda:Szalloda):
    szalloda.szobaadat()

    while True:
        menu = input(f"1. foglalás, 2. lemondás, 3. listázás")





szallodanev = Szalloda("Aranyhajó")
print(szallodanev)
