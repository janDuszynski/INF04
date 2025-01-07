"""
******************************************************
 nazwa klasy: Film
 pola: title - tytuł film,
 rentamount - ilość wyporzyczonych filmów
 metody: title_setter - ustawia wartość title na nową,
 title_getter - zwraca wartość pola title
 rentamount_getter - zwraca wartość pola rentamount
 increase_rentamout - zwiększa warość pola rentamount o 1
 show - wyświetla title oraz rentamount w uporządkowany sposób
 informacje: klasa Film ma 2 pola chronione. Dla pola title jest setter oraz getter, natomiast dla rentamount jest
 tylko getter. Można w klasie zwiększać rentamount za pomocą metody increase_rentamount. Również można wyświetlić cały
 obiekt klasy za pomocą metody show
 autor: <numer zdającego>
*****************************************************
"""


class Film:
    def __init__(self, title=None, rentamount=None):
        if title is None and rentamount is None:
            self._title = ""
            self._rentamount = 0
        elif len(title) <= 20:
            self._title = title
            self._rentamount = rentamount

    def title_setter(self, text):
        self._title = text

    def tittle_getter(self):
        return self._title

    def rentamount_getter(self):
        return self._rentamount

    def increase_rentamount(self):
        self._rentamount += 1

    def show(self):
        return f"Tytuł: {self._title}, Ilość wypożyczeń: {self._rentamount}"


if __name__ == "__main__":
    film = Film()
    print(film.show())
    film1 = Film("Kapitan Bomba", 3)
    print(film1.show())
    film1.title_setter("Egzorcysta")
    print(film1.tittle_getter())
    print(film1.rentamount_getter())
    film1.increase_rentamount()
    print(film1.rentamount_getter())
