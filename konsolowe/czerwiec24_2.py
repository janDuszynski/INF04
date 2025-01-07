"""
**********************************************
nazwa klasy: Album
opis klasy: Klasa reprezentująca album muzyczny zawierający informacje o wykonawcy, tytule albumu, liczbie utworów, roku wydania i liczbie pobrań.
parametry konstruktora:
    - artist: str, nazwa wykonawcy albumu.
    - album: str, tytuł albumu.
    - songs_number: int, liczba utworów na albumie.
    - year: int, rok wydania albumu.
    - download_number: int, liczba pobrań albumu.
zwracany typ i opis: brak
autor: <numer zdającego>
**********************************************
"""
class Album:
    def __init__(self, artist, album, songs_number, year, download_number):
        self.artist = artist
        self.album = album
        self.songs_number = songs_number
        self.year = year
        self.download_number = download_number

    """
    **********************************************
    nazwa funkcji: show_details
    opis funkcji: Wyświetla szczegóły albumu w postaci czytelnego formatu tekstowego.
    parametry: brak
    zwracany typ i opis: brak
    autor: <numer zdającego>
    **********************************************
    """
    def show_details(self):
        print(f"{self.album}\n{self.artist}\n{self.year}\n{self.songs_number}\n{self.download_number}\n")

"""
**********************************************
nazwa funkcji: convert_to_objects
opis funkcji: Przekształca dane z pliku tekstowego na listę obiektów klasy Album.
parametry: 
    - file_name: str, nazwa pliku tekstowego zawierającego dane albumów.
zwracany typ i opis: list, lista obiektów klasy Album utworzona na podstawie danych w pliku.
autor: <numer zdającego>
**********************************************
"""
def convert_to_objects(file_name):
    file = open(file_name, encoding='utf-8-sig')
    data = []
    for i in file:
        i = i.strip()
        if i:
            data.append(i)

    return create_objects(data)

"""
nazwa funkcji: create_objects
opis funkcji: Tworzy obiekty klasy Album na podstawie listy danych.
parametry: 
    - data: list, lista zawierająca dane albumów (w formie stringów) z pliku.
zwracany typ i opis: list, lista obiektów klasy Album.
autor: <numer zdającego>
"""
def create_objects(data):
    objects = []
    for i in range(0, len(data), 5):
        objects.append(Album(data[i], data[i+1], data[i+2], data[i+3], data[i+4]))

    return objects


"""
nazwa skryptu głównego: main
opis działania: Przekształca dane z pliku "Data.txt" na obiekty klasy Album, a następnie wyświetla szczegóły każdego albumu przy użyciu metody `show_details`.
parametry: brak
zwracany typ i opis: brak
autor: <numer zdającego>
"""
if __name__ == "__main__" :
    for i in convert_to_objects("Data.txt"):
        i.show_details()





