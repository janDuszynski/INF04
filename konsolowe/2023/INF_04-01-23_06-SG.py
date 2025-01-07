from math import sqrt

'''
****************************************************
 nazwa funkcji: fill_the_array
 parametry wejściowe: array - przechowuje tablice, którą chcemy wypełnić,
 arrayrange - daje informacje o wielkości tablicy
 wartość zwracana: Zwraca tablice wielkości arrayrange wypełnioną wartościami logicznymi True 
 informacje: Funkcja iteruje tablice od indexu 2 do arrayrange. Przy każdej iteracji dodaje do Tablicy element o 
 wartości True.
 autor: <numer zdającego>
****************************************************
'''


def fill_the_array(array, arrayrange):
    for x in range(2, arrayrange):
        array.append(True)


def erastotenes_algorythm(array, arrayrange):
    for i in range(int(sqrt(arrayrange)+1)):
        if array[i]:
            for j in range(2*i, arrayrange, i):
                array[j] = False


if __name__ == '__main__':
    A = [None, None]
    fill_the_array(A, 100)
    erastotenes_algorythm(A, 100)
    primes = [i for i in range(2, 100) if A[i]]
    print(primes)
