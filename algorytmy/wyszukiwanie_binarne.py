# Wyszukiwanie binarne na posortowanej tablicy - złożoność O(log n)
def szukaj_binarnie(tablica, szukana):
    lewy = 0
    prawy = len(tablica) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if tablica[srodek] == szukana:
            return srodek
        elif tablica[srodek] < szukana:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1


def szukaj_binarnie_rekurencyjnie(tablica, szukana, lewy, prawy):
    if lewy > prawy:
        return -1
    srodek = (lewy + prawy) // 2
    if tablica[srodek] == szukana:
        return srodek
    elif tablica[srodek] < szukana:
        return szukaj_binarnie_rekurencyjnie(tablica, szukana, srodek + 1, prawy)
    else:
        return szukaj_binarnie_rekurencyjnie(tablica, szukana, lewy, srodek - 1)


if __name__ == "__main__":
    liczby = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("Tablica:", liczby)
    for szukana in [23, 40]:
        print("Szukana liczba:", szukana)
        print("Iteracyjnie:", szukaj_binarnie(liczby, szukana))
        print("Rekurencyjnie:", szukaj_binarnie_rekurencyjnie(liczby, szukana, 0, len(liczby) - 1))
