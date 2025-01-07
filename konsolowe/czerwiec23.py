from math import sqrt


'''
*****************************************
nazwa funkcji: fill_list
parametry wejściowe: <A> - tablica przechowująca None
informacje: funkcja wypełnia wszystkie indeksy tablcy wartością True, poza 1 i 2 indeksem z wartością False
autor: 01234567890
*****************************************
'''
def fill_list(A, n):
    for i in range(0, n):
        A[i] = True

    A[0] = A[1] = False


'''
*****************************************
nazwa funkcji: sito
parametry wejściowe: <A> - lista o długości 100 przechowująca dwie wartości False, i na pozostałych indeksach True
wartość zwracana: lista, która zawiera wartość True w indeksach które są listami parzystymi
informacje: 
1. Pętla zewnętrzna iteruje od 2 do pierwiastka z n.
2. Dla każdego indeksu `i` o wartości True:
   * Wewnętrzna pętla oznacza jako False wszystkie wielokrotności `i`, 
     zaczynając od `i * i`.
3. Pozostałe wartości True w liście A oznaczają liczby pierwsze.
następnie wartość z tablicy o indeksie iteratora jeżeli ma wartości True usuwana ma wwsz
autor: 01234567890
*****************************************
'''
def sito(A):
    n = len(A)
    for i in range(2, int(sqrt(n)) + 1):
        if A[i]:
            for j in range(i * i, n, i):
                A[j] = False

    return A

'''
*****************************************
nazwa funkcji: print_result
parametry wejściowe: 
- array: lista wartości logicznych (`True`/`False`) o dowolnej długości
wartość zwracana: 
- brak (funkcja nie zwraca wartości, jedynie drukuje wynik)
informacje: 
- Funkcja iteruje przez podaną listę i drukuje indeksy, które mają wartość `True`.
autor: 01234567890
*****************************************
'''
def print_result(array):
    for i in range(0, len(array)):
        if array[i]:
            print(i)


A = [None] * 100
fill_list(A, 100)

print_result(sito(A))
