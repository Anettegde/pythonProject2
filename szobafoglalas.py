import szobafoglalas


class Szoba:

    def __init__(self,ar,szobasz):
        self.ar = ar
        self.szobasz = szobasz

    def foglal(self):
        print("lejárt az idő")



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
    def __init__(self):
        self.szobak = []

    def addszoba(self, szoba: Szoba):
        self.szobak.append(szoba)
    def szobaadat(self):
        self.addszoba(EgyagyasSzoba(25000,25))
        self.addszoba(KetagyasSzoba(55000,55))
        self.addszoba(EgyagyasSzoba(25000,23))

    def lista(self):
        return ' \n'.join(str(Szoba) for Szoba in self.szobak)

    def foglalni(self,fszoba):
        for szoba in self.szobak:
            if szoba.fszoba == fszoba:
                return szobafoglalas.foglal()





def foglal(szalloda:Szalloda):
    szalloda.szobaadat()

    while True:
        menu = input(f"Menü (számot vár): 1 listázás, 2 foglalás, 3 lemondás, 4 Kilépés : ")
        if menu == "1":
            print(szalloda.lista())
        elif menu =="2":
            print("itt foglalás lesz")
            fszoba = int(input("Foglalni kívánt szobaszáma: "))
            print(szalloda.foglalni(fszoba))

        elif menu =="3":
            print("lemondás lesz")
        elif menu =="4":
            print("Kilépés")
            break


#szallodanev = Szalloda("Aranyhajó")
print(f"Üdv. a Szállodában")

szalloda = Szalloda()
foglal(szalloda)




