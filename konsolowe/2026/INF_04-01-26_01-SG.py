from kosc import Kosc


def wyswietl_informacje(kosc):
    print("Liczba utworzonych instancji klasy Kosc:", Kosc.liczba_instancji)
    print("Liczba oczek wyrzucona kością:", kosc.liczba_oczek, "(" + kosc.wartosc_tekstem() + ")")
    print("Nazwa pliku z obrazem:", Kosc.nazwy_plikow[kosc.id_pliku])


if __name__ == "__main__":
    podana_wartosc = int(input("Podaj wartość wyrzuconą kością: "))
    kosc_1 = Kosc(podana_wartosc)
    wyswietl_informacje(kosc_1)

    kosc_2 = Kosc()
    wyswietl_informacje(kosc_2)
