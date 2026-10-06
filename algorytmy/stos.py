# Stos (LIFO) na liście - push, pop, peek O(1), wyszukiwanie O(n)
class Stos:
    def __init__(self):
        self.elementy = []

    def push(self, element):
        self.elementy.append(element)

    def pop(self):
        if self.czy_pusty():
            return None
        return self.elementy.pop()

    def peek(self):
        if self.czy_pusty():
            return None
        return self.elementy[len(self.elementy) - 1]

    def czy_pusty(self):
        return len(self.elementy) == 0

    def rozmiar(self):
        return len(self.elementy)

    def szukaj(self, szukana):
        for i in range(len(self.elementy) - 1, -1, -1):
            if self.elementy[i] == szukana:
                return len(self.elementy) - 1 - i
        return -1


if __name__ == "__main__":
    stos = Stos()
    for liczba in [10, 20, 30, 40]:
        stos.push(liczba)
    print("Rozmiar stosu:", stos.rozmiar())
    print("Szczyt stosu:", stos.peek())
    print("Pozycja liczby 20 od szczytu:", stos.szukaj(20))
    print("Pozycja liczby 99 od szczytu:", stos.szukaj(99))
    print("Zdejmowanie ze stosu:")
    while not stos.czy_pusty():
        print(stos.pop())
