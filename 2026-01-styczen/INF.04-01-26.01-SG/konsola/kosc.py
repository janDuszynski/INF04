import random


class Kosc:
    liczba_instancji = 0
    nazwy_plikow = ["kosc0.png", "kosc1.png", "kosc2.png", "kosc3.png", "kosc4.png", "kosc5.png", "kosc6.png"]
    nazwy_liczb = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć"]

    def __init__(self, wartosc=None):
        if wartosc is None:
            wartosc = random.randint(1, 6)
        elif wartosc not in (1, 2, 3, 4, 5, 6):
            wartosc = 0
        self.liczba_oczek = wartosc
        self.id_pliku = wartosc
        self.dostepna = True
        Kosc.liczba_instancji += 1

    def rzut(self):
        if self.dostepna:
            self.liczba_oczek = random.randint(1, 6)
            self.id_pliku = self.liczba_oczek

    def blokuj(self):
        self.dostepna = False

    def wartosc_tekstem(self):
        return Kosc.nazwy_liczb[self.liczba_oczek]
