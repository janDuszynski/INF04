# Sprawdzanie anagramów przez zliczanie liter - złożoność O(n)
def policz_litery(tekst):
    liczniki = {}
    for znak in tekst.lower():
        if znak != " ":
            if znak in liczniki:
                liczniki[znak] += 1
            else:
                liczniki[znak] = 1
    return liczniki


def czy_anagram(tekst1, tekst2):
    liczniki1 = policz_litery(tekst1)
    liczniki2 = policz_litery(tekst2)
    if len(liczniki1) != len(liczniki2):
        return False
    for litera in liczniki1:
        if litera not in liczniki2 or liczniki1[litera] != liczniki2[litera]:
            return False
    return True


if __name__ == "__main__":
    pary = [("kot", "tok"), ("Marta", "tramA"), ("ala", "alla"), ("dom", "mod")]
    for a, b in pary:
        if czy_anagram(a, b):
            print(a, "i", b, "- to anagramy")
        else:
            print(a, "i", b, "- to nie anagramy")
