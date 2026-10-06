# Test pierwszości O(sqrt(n)) i sito Eratostenesa O(n log log n)
def czy_pierwsza(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def sito_eratostenesa(n):
    pierwsza = [True] * (n + 1)
    pierwsza[0] = False
    pierwsza[1] = False
    i = 2
    while i * i <= n:
        if pierwsza[i]:
            for j in range(i * i, n + 1, i):
                pierwsza[j] = False
        i += 1
    wynik = []
    for i in range(2, n + 1):
        if pierwsza[i]:
            wynik.append(i)
    return wynik


if __name__ == "__main__":
    for liczba in [1, 2, 17, 21, 97]:
        if czy_pierwsza(liczba):
            print(liczba, "jest pierwsza")
        else:
            print(liczba, "nie jest pierwsza")
    print("Liczby pierwsze do 50:", sito_eratostenesa(50))
