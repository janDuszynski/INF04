class Film:
    def __init__(self):
        self.__tytul = ''
        self.__liczba_wypozyczen = 0

    def setTytul(self, value):
        self.__tytul = value

    def getTytul(self):
        return self.__tytul

    def getLiczbaWypozyczen(self):
        return self.__liczba_wypozyczen

    def incrementLiczbaWypozyczen(self):
        self.__liczba_wypozyczen += 1

obiekt = Film()
obiekt.setTytul("Harry Potter")
print(f"Tytuł: {obiekt.getTytul()}, Ilość Wypożyczeń: {obiekt.getLiczbaWypozyczen()}")
obiekt.incrementLiczbaWypozyczen()
print(f"Tytuł: {obiekt.getTytul()}, Ilość Wypożyczeń: {obiekt.getLiczbaWypozyczen()}")
