import random


class FindWithGuardian:
    def __init__(self, listt, lookingforr):
        self.listt = listt
        self.lookingforr = lookingforr

    '''
    ******************************************************
     nazwa funkcji: fill_array
     argumenty: self - przechowuje ona pola klasy FindWithGuardian: listt oraz lookingforr
     typ zwracany: tablica, zwracamy wepłnioną tablicę liczbami pseudolosowymi z zakresu 1-100
     informacje: Na początku funkcja ustawia listt na pustą tablicę. Następnie pętla for wykonuje się 50 razy. Podczas
     każdego przejścia dodaje do tablicy liczbę pseudolosową z zakresu 1-100.
     autor: <numer zdającego>
    *****************************************************
    '''
    def fill_array(self):
        self.listt = []
        for i in range(50):
            self.listt.append(random.randint(1, 100))
        return self.listt

    '''
    ******************************************************
     nazwa funkcji: find
     argumenty: self - przechowuje ona pola klasy FindWithGuardian: listt oraz lookingforr
     typ zwracany: string, zwraca komunikat o tym, czy poszukiwana liczba znajduje się w tablicy czy nie
     informacje: Na początku funkcja tworzy wartownika o wartości podanej przez użtykownika i umieszcza go na końcu
     tablicy. Następnie pętla for iteruje po tablicy listt. Jeżeli liczba w tablicy będzię równej poszukiwanej, to
     sprawdza czy znaleziona liczba nie jest wartownikiem. Jeżeli nie jest to wartownik, to jest wypisywany komunikat o
     jej znalezieniu i podaje pozycje na której się znajduje. W przeciwnym przypadku program wyświetla komunikat iż w 
     tablicy nie znajduje się szukana liczba.
     autor: <numer zdającego>
    *****************************************************
    '''
    def find(self):
        wanted = self.lookingforr
        self.listt.append(wanted)

        for i in range(len(self.listt)):
            if self.listt[i] == wanted:
                if i == len(self.listt) - 1:
                    return "W tej tablicy nie ma liczby " + str(self.lookingforr)
                else:
                    return ("W tej tablicy jest liczba " + str(self.lookingforr) + " i znajduje się na indexie: "
                            + str(i))


if __name__ == '__main__':
    array = []
    preventError = True
    while preventError:
        lookingfor = int(input("Podaj liczbę z zakresu 1-100, którą chcesz znaleść: "))
        if 1 <= lookingfor <= 100:
            preventError = False
            finder = FindWithGuardian(array, lookingfor)
            print(finder.fill_array())
            print(finder.find())
        else:
            print("Błąd; spróbuj ponownie")
