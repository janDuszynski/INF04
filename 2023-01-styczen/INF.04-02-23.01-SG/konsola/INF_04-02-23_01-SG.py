"""
************************************************
 klasa: Notatka
 opis: Klasa jest reprezentacją notatki składającej się z tytuło oraz treśći
 pola: id - przechowuje unikalny identyfikator notatki,
 title - przechowuje tytuł notatki,
 content -przechowuje treść notatki
 autor: <numer zdającego>
************************************************
"""


class Notatka:
    licznik_notatek = 0

    def __init__(self, title, content):
        Notatka.licznik_notatek += 1

        self.__id = Notatka.licznik_notatek
        self._title = title
        self._content = content

    def show_note(self):
        print(f"Tytuł: {self._title}\nTreść: {self._content}")

    def show_note_data(self):
        print(f"{self.__id};{self._title};{self._content}")


if __name__ == '__main__':
    notatka1 = Notatka("Seks", "Kopulacja jest potrzebna do przeżyciu każdego gatunku ssaka")
    notatka2 = Notatka("Arczi", "Każdy z Dębca to przestępca")
    notatka1.show_note()
    notatka1.show_note_data()
    notatka2.show_note()
    notatka2.show_note_data()
