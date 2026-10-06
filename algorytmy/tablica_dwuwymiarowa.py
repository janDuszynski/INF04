# Operacje na tablicy dwuwymiarowej (macierzy) - złożoność O(n*m)
import random


def wypelnij_losowo(wiersze, kolumny):
    tablica = []
    for i in range(wiersze):
        wiersz = []
        for j in range(kolumny):
            wiersz.append(random.randint(1, 9))
        tablica.append(wiersz)
    return tablica


def wyswietl(tablica):
    for wiersz in tablica:
        for element in wiersz:
            print(element, end="\t")
        print()


def sumy_wierszy(tablica):
    sumy = []
    for wiersz in tablica:
        suma = 0
        for element in wiersz:
            suma += element
        sumy.append(suma)
    return sumy


def sumy_kolumn(tablica):
    sumy = []
    for j in range(len(tablica[0])):
        suma = 0
        for i in range(len(tablica)):
            suma += tablica[i][j]
        sumy.append(suma)
    return sumy


def transpozycja(tablica):
    wynik = []
    for j in range(len(tablica[0])):
        wiersz = []
        for i in range(len(tablica)):
            wiersz.append(tablica[i][j])
        wynik.append(wiersz)
    return wynik


def przekatna_glowna(tablica):
    wynik = []
    for i in range(len(tablica)):
        wynik.append(tablica[i][i])
    return wynik


def przekatna_poboczna(tablica):
    n = len(tablica)
    wynik = []
    for i in range(n):
        wynik.append(tablica[i][n - 1 - i])
    return wynik


if __name__ == "__main__":
    macierz = wypelnij_losowo(4, 4)
    print("Macierz:")
    wyswietl(macierz)
    print("Sumy wierszy:", sumy_wierszy(macierz))
    print("Sumy kolumn:", sumy_kolumn(macierz))
    print("Przekątna główna:", przekatna_glowna(macierz))
    print("Przekątna poboczna:", przekatna_poboczna(macierz))
    print("Transpozycja:")
    wyswietl(transpozycja(macierz))
