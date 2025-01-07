class SortByChoosing:
    def __init__(self, listt):
        self.listt = listt

    def show_list(self):
        print(self.__sort_by_choosing())

    def show_max_index(self):
        print(self.__list_max())

    '''
    /********************************************************
    * nazwa funkcji: list_max
    * parametry wejściowe: self - przechowuje pole listt klasy SortByChoosing; i - przekazuje index, od którego ma 
    zacząć iteracje(domyślnie ustawiony na 0).
    * wartość zwracana: zwraca index tablicy z największym elementem w postaci zmiennej max_index.
    * autor: <numer PESEL zdającego>
    * ****************************************************/
    '''
    def __list_max(self, i=0):
        max_index = i
        for j in range(i, len(self.listt)):
            if self.listt[j] > self.listt[max_index]:
                max_index = j
        return max_index

    '''
    /********************************************************
    * nazwa funkcji: sort_by_choosing
    * parametry wejściowe: self - przechowuje pole listt klasy SortByChoosing.
    * wartość zwracana: zwraca posortowaną tablice listt klasy SortByChoosing.
    * autor: <numer PESEL zdającego>
    * ****************************************************/
    '''
    def __sort_by_choosing(self):
        for i in range(len(self.listt)):
            max_index = self.__list_max(i)
            self.listt[i], self.listt[max_index] = self.listt[max_index], self.listt[i]
        return self.listt


if __name__ == '__main__':
    array = []
    print("Stwórz tablice 10 elementową")
    for i in range(10):
        number = int(input("Podaj " + str(i) + " liczbę to tablicy, pozostało " + str(10-i) + " : "))
        array.append(number)

    sorted_array = SortByChoosing(array)
    print("Tablica przed sortowaniem: ", array)
    print("Index największego elementu: ", end=" ")
    sorted_array.show_max_index()
    print("Posortowana tablica: ", end=" ")
    sorted_array.show_list()
