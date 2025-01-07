'''
********************************************
nazwa_funkcji: nwd
opis funkcji: funkcja oblicza największy wspólny dzielnik korzystając z algorytmu euklidesa
parametry:
    a - pierwsza liczba całkowita dla której będzie liczony wspólny dzielnik
    b - druga liczba całkowita dla której będzie liczony wspólny dzielnik
zwracany typ i opis: liczba całkowita - największy wspólny dzielnik parametrów a i b
autor: 01234567890
********************************************
'''


def nwd(a : int, b : int):
    while a != b:
        if a > b:
            a -=b
        else:
            b -=a
    return a



a = int(input("Wprowadź A"))
b = int(input("Wprowadź B"))


print(nwd(a, b))