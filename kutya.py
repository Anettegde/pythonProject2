class Kutya:
    def __init__(self, nev, kora, faja):
        self.nev = nev
        self.kora = kora
        self.faja = faja

    def ugat(self):
        print(f"{self.nev} mondja: Vau!")

    def emberi_evekben(self):
        kora = self.kora
        emberikora = int(kora) * 2
        print(f"{kora} {emberikora}")


dog = Kutya("Bodri", "2", "Kutya")
dog.ugat()
dog.emberi_evekben()