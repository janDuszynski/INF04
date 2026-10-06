# Sortowanie przez zliczanie (liczby naturalne) - złożoność O(n + k), k to największa liczba
def sortuj_przez_zliczanie(tablica):
    maksimum = tablica[0]
    for liczba in tablica:
        if liczba > maksimum:
            maksimum = liczba

    liczniki = [0] * (maksimum + 1)
    for liczba in tablica:
        liczniki[liczba] += 1

    wynik = []
    for wartosc in range(maksimum + 1):
        for _ in range(liczniki[wartosc]):
            wynik.append(wartosc)
    return wynik


if __name__ == "__main__":
    liczby = [4, 2, 2, 8, 3, 3, 1, 0, 7, 4]
    print("Przed sortowaniem:", liczby)
    print("Po sortowaniu:", sortuj_przez_zliczanie(liczby))
