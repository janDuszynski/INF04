# Szukanie minimum i maksimum - złożoność O(n)
def znajdz_minimum(tablica):
    indeks = 0
    for i in range(1, len(tablica)):
        if tablica[i] < tablica[indeks]:
            indeks = i
    return tablica[indeks], indeks


def znajdz_maksimum(tablica):
    indeks = 0
    for i in range(1, len(tablica)):
        if tablica[i] > tablica[indeks]:
            indeks = i
    return tablica[indeks], indeks


if __name__ == "__main__":
    liczby = [17, 4, 25, -3, 42, 8, 11]
    print("Tablica:", liczby)
    wartosc, indeks = znajdz_minimum(liczby)
    print("Minimum:", wartosc, "na indeksie", indeks)
    wartosc, indeks = znajdz_maksimum(liczby)
    print("Maksimum:", wartosc, "na indeksie", indeks)
