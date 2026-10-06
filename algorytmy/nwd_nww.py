# NWD (algorytm Euklidesa) i NWW - złożoność wersji z modulo O(log n)
def nwd_odejmowanie(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def nwd_modulo(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def nwd_rekurencyjnie(a, b):
    if b == 0:
        return a
    return nwd_rekurencyjnie(b, a % b)


def nww(a, b):
    return a * b // nwd_modulo(a, b)


if __name__ == "__main__":
    a = 48
    b = 18
    print("Liczby:", a, b)
    print("NWD przez odejmowanie:", nwd_odejmowanie(a, b))
    print("NWD przez modulo:", nwd_modulo(a, b))
    print("NWD rekurencyjnie:", nwd_rekurencyjnie(a, b))
    print("NWW:", nww(a, b))
