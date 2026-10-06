# Szyfr Vigenere'a (alfabet łaciński) - złożoność O(n)
def przesun_litere(znak, przesuniecie):
    if znak.isupper():
        poczatek = 65
    else:
        poczatek = 97
    return chr((ord(znak) - poczatek + przesuniecie) % 26 + poczatek)


def szyfruj(tekst, klucz, kierunek=1):
    wynik = ""
    klucz = klucz.lower()
    k = 0
    for znak in tekst:
        if znak.isascii() and znak.isalpha():
            przesuniecie = (ord(klucz[k % len(klucz)]) - 97) * kierunek
            wynik += przesun_litere(znak, przesuniecie)
            k += 1
        else:
            wynik += znak
    return wynik


def deszyfruj(tekst, klucz):
    return szyfruj(tekst, klucz, -1)


if __name__ == "__main__":
    tekst = "Attack at Dawn, 5 o'clock!"
    klucz = "lemon"
    zaszyfrowany = szyfruj(tekst, klucz)
    print("Tekst:", tekst)
    print("Zaszyfrowany:", zaszyfrowany)
    print("Odszyfrowany:", deszyfruj(zaszyfrowany, klucz))
