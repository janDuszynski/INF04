import random

SMALL_LETTERS = "abcdefghijklmnopqrstuvwxyz"
BIG_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIACRITIC_LETTERS = "ąęłńóśżźĄĘŁŃÓŚŻŹ"
DIGITS = "0123456789"
SPECIAL_CHARS = "!@#$%^&*()_+"

'''
****************************************************
 nazwa funkcji:              generate_password
 opis funkcji:               Funkcja losuje 3 małe litery, 3 wielkie litery, 2 litery ze znakami diakrytycznymi,
                             2 cyfry i 2 znaki specjalne. Następnie miesza wylosowane znaki, aby każdy znajdował
                             się w losowym miejscu, i łączy je w 12-znakowe hasło
 parametry:                  brak
 zwracany typ i opis:        str - wygenerowane 12-znakowe hasło
 autor:                      <numer zdającego>
****************************************************
'''


def generate_password():
    characters = []
    for _ in range(3):
        characters.append(random.choice(SMALL_LETTERS))
        characters.append(random.choice(BIG_LETTERS))
    for _ in range(2):
        characters.append(random.choice(DIACRITIC_LETTERS))
        characters.append(random.choice(DIGITS))
        characters.append(random.choice(SPECIAL_CHARS))

    random.shuffle(characters)

    password = ""
    for character in characters:
        password += character
    return password


if __name__ == "__main__":
    print("Wygenerowane hasła:")
    for i in range(5):
        print(f"{i + 1}. {generate_password()}")
