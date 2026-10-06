# Losowanie k różnych liczb z zakresu 1..n (np. lotto) - złożoność O(k) średnio
import random


def losuj_bez_powtorzen(k, n):
    wylosowane = [False] * (n + 1)
    wynik = []
    while len(wynik) < k:
        liczba = random.randint(1, n)
        if not wylosowane[liczba]:
            wylosowane[liczba] = True
            wynik.append(liczba)
    return wynik


if __name__ == "__main__":
    print("Lotto 6 z 49:", losuj_bez_powtorzen(6, 49))
    print("Lotto 6 z 49:", losuj_bez_powtorzen(6, 49))
    print("Wszystkie liczby od 1 do 10 w losowej kolejności:", losuj_bez_powtorzen(10, 10))
