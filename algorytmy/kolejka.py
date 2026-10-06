# Kolejka (FIFO) - enqueue, dequeue, peek, wyszukiwanie O(n)
class Kolejka:
    def __init__(self):
        self.elementy = []

    def enqueue(self, element):
        self.elementy.append(element)

    def dequeue(self):
        if self.czy_pusta():
            return None
        pierwszy = self.elementy[0]
        for i in range(1, len(self.elementy)):
            self.elementy[i - 1] = self.elementy[i]
        self.elementy.pop()
        return pierwszy

    def peek(self):
        if self.czy_pusta():
            return None
        return self.elementy[0]

    def czy_pusta(self):
        return len(self.elementy) == 0

    def rozmiar(self):
        return len(self.elementy)

    def szukaj(self, szukana):
        for i in range(len(self.elementy)):
            if self.elementy[i] == szukana:
                return i
        return -1


if __name__ == "__main__":
    kolejka = Kolejka()
    for osoba in ["Ania", "Basia", "Czarek", "Darek"]:
        kolejka.enqueue(osoba)
    print("Rozmiar kolejki:", kolejka.rozmiar())
    print("Pierwszy w kolejce:", kolejka.peek())
    print("Pozycja Czarka:", kolejka.szukaj("Czarek"))
    print("Pozycja Ewy:", kolejka.szukaj("Ewa"))
    print("Obsługa kolejki:")
    while not kolejka.czy_pusta():
        print(kolejka.dequeue())
