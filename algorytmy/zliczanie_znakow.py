# Zliczanie samogłosek, spółgłosek i cyfr w tekście - złożoność O(n)
SAMOGLOSKI = "aąeęioóuy"


def zlicz_znaki(tekst):
    samogloski = 0
    spolgloski = 0
    cyfry = 0
    for znak in tekst.lower():
        if znak.isdigit():
            cyfry += 1
        elif znak.isalpha():
            if znak in SAMOGLOSKI:
                samogloski += 1
            else:
                spolgloski += 1
    return samogloski, spolgloski, cyfry


if __name__ == "__main__":
    tekst = "Zażółć gęślą jaźń 2026"
    samogloski, spolgloski, cyfry = zlicz_znaki(tekst)
    print("Tekst:", tekst)
    print("Samogłosek:", samogloski)
    print("Spółgłosek:", spolgloski)
    print("Cyfr:", cyfry)
