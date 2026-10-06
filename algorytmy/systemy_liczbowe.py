# Zamiana systemów liczbowych (podstawa 2..16) - złożoność O(log n)
CYFRY = "0123456789ABCDEF"


def z_dziesietnego(liczba, podstawa):
    if liczba == 0:
        return "0"
    wynik = ""
    while liczba > 0:
        reszta = liczba % podstawa
        wynik = CYFRY[reszta] + wynik
        liczba = liczba // podstawa
    return wynik


def na_dziesietny(napis, podstawa):
    wynik = 0
    for znak in napis.upper():
        for wartosc in range(podstawa):
            if CYFRY[wartosc] == znak:
                wynik = wynik * podstawa + wartosc
    return wynik


if __name__ == "__main__":
    liczba = 2026
    for podstawa in [2, 8, 16]:
        zapis = z_dziesietnego(liczba, podstawa)
        print(liczba, "w systemie o podstawie", podstawa, "to", zapis)
        print("Z powrotem na dziesiętny:", na_dziesietny(zapis, podstawa))
