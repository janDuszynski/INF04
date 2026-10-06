import random


class Tablica:
    def __init__(self, rozmiar):
        self.__liczba_elementow = rozmiar
        self.__tab = []
        for i in range(rozmiar):
            self.__tab.append(random.randint(1, 1000))

    def wyswietl(self):
        for i in range(self.__liczba_elementow):
            print(f'{i}: {self.__tab[i]}')

    def szukaj(self, wartosc):
        for i in range(self.__liczba_elementow):
            if self.__tab[i] == wartosc:
                return i
        return -1

    def wyswietl_nieparzyste(self):
        ile = 0
        for i in range(self.__liczba_elementow):
            if self.__tab[i] % 2 == 1:
                print(self.__tab[i])
                ile += 1
        return ile

    """
    **********************************************
    nazwa metody: srednia
    opis metody: metoda liczy średnią arytmetyczną wszystkich wartości w tablicy
    parametry: brak
    zwracany typ i opis: float, metoda zwraca średnią arytmetyczną wartości w tablicy
    autor: <numer zdającego>
    ***********************************************
    """
    def srednia(self):
        suma = 0
        for i in range(self.__liczba_elementow):
            suma += self.__tab[i]
        return suma / self.__liczba_elementow


if __name__ == "__main__":
    tablica = Tablica(25)

    print('Elementy tablicy:')
    tablica.wyswietl()

    szukana = 500
    indeks = tablica.szukaj(szukana)
    if indeks != -1:
        print(f'Wartość {szukana} znaleziono pod indeksem: {indeks}')

    print('Liczby nieparzyste:')
    ile_nieparzystych = tablica.wyswietl_nieparzyste()
    print(f'Liczba nieparzystych elementów: {ile_nieparzystych}')

    print(f'Średnia wartość elementów: {tablica.srednia()}')
