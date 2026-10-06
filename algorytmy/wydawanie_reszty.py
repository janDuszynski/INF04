# Wydawanie reszty - algorytm zachłanny, kwoty w groszach, złożoność O(liczba nominałów)
NOMINALY = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]


def wydaj_reszte(grosze):
    reszta = {}
    for nominal in NOMINALY:
        ile = grosze // nominal
        if ile > 0:
            reszta[nominal] = ile
            grosze = grosze % nominal
    return reszta


if __name__ == "__main__":
    kwota = 237.83
    grosze = round(kwota * 100)
    print("Reszta do wydania:", kwota, "zł")
    wynik = wydaj_reszte(grosze)
    for nominal in wynik:
        if nominal >= 100:
            print(nominal // 100, "zł x", wynik[nominal])
        else:
            print(nominal, "gr x", wynik[nominal])
