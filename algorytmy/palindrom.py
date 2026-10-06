# Sprawdzanie palindromu - złożoność O(n)
def czy_palindrom(tekst):
    litery = ""
    for znak in tekst:
        if znak != " ":
            litery += znak.lower()

    lewy = 0
    prawy = len(litery) - 1
    while lewy < prawy:
        if litery[lewy] != litery[prawy]:
            return False
        lewy += 1
        prawy -= 1
    return True


if __name__ == "__main__":
    for tekst in ["Kajak", "Kobyła ma mały bok", "Ala ma kota", "Zakopane"]:
        if czy_palindrom(tekst):
            print(tekst, "- to palindrom")
        else:
            print(tekst, "- to nie palindrom")
