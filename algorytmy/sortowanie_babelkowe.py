# Sortowanie bąbelkowe - złożoność O(n^2), pesymistycznie i średnio
def sortuj_babelkowo(tablica):
    n = len(tablica)
    for i in range(n - 1):
        zamiana = False
        for j in range(n - 1 - i):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
                zamiana = True
        if not zamiana:
            break
    return tablica


if __name__ == "__main__":
    liczby = [64, 34, 25, 12, 22, 11, 90, 5]
    print("Przed sortowaniem:", liczby)
    sortuj_babelkowo(liczby)
    print("Po sortowaniu:", liczby)
