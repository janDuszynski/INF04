class DataStructure:
    def __init__(self, artist, album, songsnumber, year, downloadnumber):
        self.artist = artist.strip()
        self.album = album.strip()
        self.songsnumber = int(songsnumber.strip())
        self.year = int(year.strip())
        self.downloadnumber = int(downloadnumber.strip())

    """
    **********************************************
    nazwa funkcji: show_data
    opis funkcji: Wypisuje wszystie informacje o obiekcie DataStructure
    parametry: self - przechowuje pola klasy DataStructure
    zwracany typ i opis: string, zwraca dane klasy DataStructure, każde pole zapisane w osobnej linii
    autor: <numer zdającego>
    ***********************************************
    """

    def show_data(self):
        return f"{self.artist}\n{self.album}\n{self.songsnumber}\n{self.year}\n{self.downloadnumber}\n"


def fill_the_array(array):
    with open('Data.txt', encoding="utf-8") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 6):
            album = DataStructure(lines[i], lines[i + 1], lines[i + 2], lines[i + 3], lines[i + 4])
            array.append(album)
    for album in array:
        print(album.show_data())


if __name__ == '__main__':
    album_list = []
    fill_the_array(album_list)
