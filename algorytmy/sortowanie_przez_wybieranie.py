# Sortowanie przez wybieranie - złożoność O(n^2)
def sortuj_rosnaco(tablica):
    n = len(tablica)
    for i in range(n - 1):
        indeks_min = i
        for j in range(i + 1, n):
            if tablica[j] < tablica[indeks_min]:
                indeks_min = j
        tablica[i], tablica[indeks_min] = tablica[indeks_min], tablica[i]
    return tablica


def sortuj_malejaco(tablica):
    n = len(tablica)
    for i in range(n - 1):
        indeks_max = i
        for j in range(i + 1, n):
            if tablica[j] > tablica[indeks_max]:
                indeks_max = j
        tablica[i], tablica[indeks_max] = tablica[indeks_max], tablica[i]
    return tablica


if __name__ == "__main__":
    liczby = [29, 10, 14, 37, 13, 5, 42, 8]
    print("Przed sortowaniem:", liczby)
    print("Po sortowaniu rosnaco:", sortuj_rosnaco(liczby[:]))
    print("Po sortowaniu malejaco:", sortuj_malejaco(liczby[:]))
