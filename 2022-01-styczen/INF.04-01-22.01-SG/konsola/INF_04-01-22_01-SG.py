class SelectionSort:
    def __init__(self):
        self.numbers = [0] * 10

    '''
    ******************************************************
     nazwa funkcji: read_numbers
     parametry wejściowe: brak
     wartość zwracana: brak, funkcja wczytuje 10 liczb z klawiatury do tablicy
     autor: <numer zdającego>
    ******************************************************
    '''
    def read_numbers(self):
        print("Podaj 10 liczb całkowitych:")
        for i in range(10):
            self.numbers[i] = int(input())

    '''
    ******************************************************
     nazwa funkcji: __find_max_index
     parametry wejściowe: start - indeks, od którego szukana jest wartość największa
     wartość zwracana: indeks największej wartości w tablicy od indeksu start do końca
     autor: <numer zdającego>
    ******************************************************
    '''
    def __find_max_index(self, start):
        max_index = start
        for i in range(start + 1, len(self.numbers)):
            if self.numbers[i] > self.numbers[max_index]:
                max_index = i
        return max_index

    '''
    ******************************************************
     nazwa funkcji: sort
     parametry wejściowe: brak
     wartość zwracana: brak, funkcja sortuje tablicę malejąco metodą przez wybieranie
     autor: <numer zdającego>
    ******************************************************
    '''
    def sort(self):
        for i in range(len(self.numbers) - 1):
            max_index = self.__find_max_index(i)
            self.numbers[i], self.numbers[max_index] = self.numbers[max_index], self.numbers[i]

    def print_numbers(self):
        print("Posortowana tablica:")
        for number in self.numbers:
            print(number)


if __name__ == '__main__':
    selection_sort = SelectionSort()
    selection_sort.read_numbers()
    selection_sort.sort()
    selection_sort.print_numbers()
