class Szoba:

    def __init__(self,ar,szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    pass

class KetagyasSzoba(Szoba):
    pass

class Foglalas:
    pass


class Szalloda:

    def __init__(self, nev):
        self.nev = nev

    def __str__(self):
       return f"A szálloda neve: {self.nev}"


szallodanev = Szalloda("Aranyhajó")
print(szallodanev)
