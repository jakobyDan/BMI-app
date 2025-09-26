class BMI:

    def __init__(self, hmotnost, vyska):
        self.hmotnost = hmotnost
        self.vyska = vyska

    def vypocti(self):
        return self.hmotnost / (self.vyska ** 2)

    def get_kategorie(self):
        if self.vypocti() < 16.5:
            return "těžká podvýživa"
        elif self.vypocti() < 18.5:
            return "podváha"
        elif self.vypocti() < 25:
            return "ideální váha"
        elif self.vypocti() < 30:
            return "nadváha"
        elif self.vypocti() < 35:
            return "mírná obezita"
        elif self.vypocti() < 40:
            return "střední obezita"
        else:
            return "morbidní obezita"



