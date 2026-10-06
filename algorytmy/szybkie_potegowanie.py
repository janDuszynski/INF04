# Szybkie potęgowanie (dziel i zwyciężaj) - złożoność O(log n)
def potega(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    if wykladnik % 2 == 0:
        polowa = potega(podstawa, wykladnik // 2)
        return polowa * polowa
    return podstawa * potega(podstawa, wykladnik - 1)


if __name__ == "__main__":
    print("2^10 =", potega(2, 10))
    print("3^13 =", potega(3, 13))
    print("7^0 =", potega(7, 0))
    print("2^100 =", potega(2, 100))
