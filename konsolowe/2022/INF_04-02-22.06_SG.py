class Osoba:
    liczba_obiektow = 0

    def __init__(self, id=None, imie=None):
        if id is None and imie is None:
            self.__id = 0
            self.__imie = ""
        elif isinstance(id, Osoba):
            self.__id = id.__id
            self.__imie = id.__imie
        else:
            self.__id = id
            self.__imie = imie
        Osoba.liczba_obiektow += 1

    def get_id(self):
        return self.__id

    def get_imie(self):
        return self.__imie

    @staticmethod
    def get_liczba_obiektow():
        return Osoba.liczba_obiektow

    def greeting(self, content):
        if self.get_imie() == "":
            return "Brak danych"
        else:
            return "Cześć " + str(content) + ", mam na imię " + str(Osoba.get_imie(self))


if __name__ == '__main__':
    print(f"Liczba zarejstrowanych osoób to{Osoba.get_liczba_obiektow()}")
    osoba1 = Osoba()
    osoba2_id = int(input("Podaj id: "))
    osoba2_imie = str(input("Podaj imie: "))
    osoba2 = Osoba(osoba2_id, osoba2_imie)
    osoba3 = Osoba(osoba2)
    print(osoba1.greeting("Jan"))
    print(osoba2.greeting("Jan"))
    print(osoba3.greeting("Jan"))
    print(f"Liczba zarejstrowanych osoób to{Osoba.get_liczba_obiektow()}")

    print(f"ID osoby 1: {osoba1.get_id()}, Imię: {osoba1.get_imie()}")
    print(f"ID osoby 2: {osoba2.get_id()}, Imię: {osoba2.get_imie()}")
    print(f"ID osoby 3: {osoba3.get_id()}, Imię: {osoba3.get_imie()}")


