# Silnia iteracyjnie i rekurencyjnie - złożoność O(n)
def silnia_iteracyjnie(n):
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik


def silnia_rekurencyjnie(n):
    if n <= 1:
        return 1
    return n * silnia_rekurencyjnie(n - 1)


if __name__ == "__main__":
    for n in range(0, 11):
        print(str(n) + "! =", silnia_iteracyjnie(n), silnia_rekurencyjnie(n))
