class Etel:

    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar

class Etterem:

    def __init__(self,menu_elem,nev):
        self.menu_elem = menu_elem
        self.nev = nev

    def __str__(self):
        return f"Az étterem neve: {self.nev}"

    def __add__(self, other):
        if isinstance(other,Etel):
            self.menu_elem.append(other)
        else:
            print("Nem az")

    def getmenuitem(self):
        for menu_elem in self.menu_elem:
            print(f"{menu_elem.nev}............{menu_elem.ar} Ft")


etel1 = Etel('Hambi',100)
etel2 = Etel('Szendvics', 870)
my_menu = [etel1,etel2]

my_restaurant = Etterem(my_menu,"Kisbojtár")
my_restaurant.getmenuitem()


for i in range(2):
    etelneve = input("Add meg az étel nevét ")
    etelara = int(input("Add meg az árát: "))
    if etelara<0 or etelara>10000:
        print("Nem megfelelő ár")
        break
    else:
        #my_restaurant.menu_elem.append(Etel(etelneve,etelara))
        my_restaurant + Etel(etelneve, etelara)

#my_restaurant + Etel(etelneve, etelara)

#my_restaurant.getmenuitem()
my_restaurant + "szoveg"

my_restaurant.getmenuitem()



my_etel = Etel("húsleves",320)

print(my_restaurant)


