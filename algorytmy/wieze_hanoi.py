# Wieże Hanoi (rekurencja) - złożoność O(2^n), liczba ruchów 2^n - 1
def hanoi(n, z, na, pomocniczy):
    if n == 0:
        return
    hanoi(n - 1, z, pomocniczy, na)
    print("Przenieś krążek", n, "z", z, "na", na)
    hanoi(n - 1, pomocniczy, na, z)


if __name__ == "__main__":
    liczba_krazkow = 3
    print("Wieże Hanoi dla", liczba_krazkow, "krążków:")
    hanoi(liczba_krazkow, "A", "C", "B")
