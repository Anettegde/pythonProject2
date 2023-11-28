class Jegy:
    def __init__(self, teszte, ffe):
        self.teszte = teszte
        self.ffe = ffe

    def erdemjegy(self):
        teszteredm = int(self.teszte)
        fejleredm = int(self.ffe)

        print(f"jegy: {(teszteredm + fejleredm) / 2}")


jegye = Jegy("3", "4")
jegye.erdemjegy()

