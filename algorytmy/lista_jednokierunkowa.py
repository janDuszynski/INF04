# Lista jednokierunkowa - dodawanie na początek O(1), na koniec, usuwanie i wyszukiwanie O(n)
class Wezel:
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.nastepny = None


class Lista:
    def __init__(self):
        self.glowa = None

    def dodaj_na_poczatek(self, wartosc):
        wezel = Wezel(wartosc)
        wezel.nastepny = self.glowa
        self.glowa = wezel

    def dodaj_na_koniec(self, wartosc):
        wezel = Wezel(wartosc)
        if self.glowa is None:
            self.glowa = wezel
            return
        aktualny = self.glowa
        while aktualny.nastepny is not None:
            aktualny = aktualny.nastepny
        aktualny.nastepny = wezel

    def usun(self, wartosc):
        poprzedni = None
        aktualny = self.glowa
        while aktualny is not None:
            if aktualny.wartosc == wartosc:
                if poprzedni is None:
                    self.glowa = aktualny.nastepny
                else:
                    poprzedni.nastepny = aktualny.nastepny
                return True
            poprzedni = aktualny
            aktualny = aktualny.nastepny
        return False

    def wyszukaj(self, wartosc):
        aktualny = self.glowa
        indeks = 0
        while aktualny is not None:
            if aktualny.wartosc == wartosc:
                return indeks
            aktualny = aktualny.nastepny
            indeks += 1
        return -1

    def wyswietl(self):
        aktualny = self.glowa
        while aktualny is not None:
            print(aktualny.wartosc, end=" -> ")
            aktualny = aktualny.nastepny
        print("None")


if __name__ == "__main__":
    lista = Lista()
    lista.dodaj_na_koniec(2)
    lista.dodaj_na_koniec(3)
    lista.dodaj_na_koniec(4)
    lista.dodaj_na_poczatek(1)
    print("Lista po dodaniu elementów:")
    lista.wyswietl()
    print("Indeks liczby 3:", lista.wyszukaj(3))
    print("Indeks liczby 9:", lista.wyszukaj(9))
    lista.usun(3)
    print("Lista po usunięciu liczby 3:")
    lista.wyswietl()
