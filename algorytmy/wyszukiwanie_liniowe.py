# Wyszukiwanie liniowe (zwykłe i z wartownikiem) - złożoność O(n)
def szukaj_liniowo(tablica, szukana):
    for i in range(len(tablica)):
        if tablica[i] == szukana:
            return i
    return -1


def szukaj_z_wartownikiem(tablica, szukana):
    n = len(tablica)
    tablica.append(szukana)
    i = 0
    while tablica[i] != szukana:
        i += 1
    tablica.pop()
    if i < n:
        return i
    return -1


if __name__ == "__main__":
    liczby = [7, 3, 9, 1, 5, 8, 2]
    for szukana in [5, 4]:
        print("Szukana liczba:", szukana)
        print("Liniowo:", szukaj_liniowo(liczby, szukana))
        print("Z wartownikiem:", szukaj_z_wartownikiem(liczby, szukana))
