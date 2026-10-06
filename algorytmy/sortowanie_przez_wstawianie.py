# Sortowanie przez wstawianie - złożoność O(n^2), dla prawie posortowanych danych O(n)
def sortuj_przez_wstawianie(tablica):
    for i in range(1, len(tablica)):
        klucz = tablica[i]
        j = i - 1
        while j >= 0 and tablica[j] > klucz:
            tablica[j + 1] = tablica[j]
            j -= 1
        tablica[j + 1] = klucz
    return tablica


if __name__ == "__main__":
    liczby = [12, 11, 13, 5, 6, 1, 9, 3]
    print("Przed sortowaniem:", liczby)
    sortuj_przez_wstawianie(liczby)
    print("Po sortowaniu:", liczby)
