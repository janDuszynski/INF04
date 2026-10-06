class EuklidesAlgorythm:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    '''
    **********************************************
    nazwa funkcji: nwd
    opis funkcji: Na początku przypisujemy wartości a i b do x oraz y. Następnie jest pętla, która sprawdza czy x oraz y
    są takie same. Jeśli nie są, to sprawdzamy, która z liczb jest większa i od niej odejmujemy mniejszą. Pętla wykonuje
    tą sekwencje dopóki liczby x oraz y są takie same. Na sam koniec zwraca nwd, które jest zapisane w liczbie x.
    parametry: self - przechowuje pola klasy a oraz b, czyli dwóch liczb całkowitych dodatnich 
    zwracany typ i opis: int, zwrócony wynik to największy wspólny licznik liczb a oraz b
    autor: <numer zdającego>
    ***********************************************
    '''
    def nwd(self):
        x = self.a
        y = self.b
        while x != y:
            if x > y:
                x = x-y
            else:
                y = y-x
        return x


if __name__ == '__main__':
    preventError = True
    while preventError:
        firstNumber = int(input("Podaj 1szą liczbę: "))
        secondNumber = int(input("Podaj 2gą liczbę: "))
        if firstNumber > 0 and secondNumber > 0:
            result = EuklidesAlgorythm(firstNumber, secondNumber)
            print(result.nwd())
            preventError = False
