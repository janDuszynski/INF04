def check_pesel(pesel='55030101193'):
    pesel_number_separeted = separete(pesel)
    pesel_number_weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    s = sum(pesel_number_separeted[i]*pesel_number_weight[i] for i in range(10))
    m = s % 10
    r = 0
    if m != 0:
        r = 10-m
    if pesel_number_separeted[10] == r:
        return True
    else:
        return False


"""
**********************************************
nazwa funkcji: check_gender
opis funkcji: funkcja sprawdza 10 cyfrę PESELu i na jej podstawie ocenia czy osoba jest kobietą czy mężczyzną
parametry: pesel - numer PESEL (domyślnie ustawiony na 55030101193)
zwracany typ i opis: char, funkcja zwraca 'K', jeżeli użytkownik PESELu jest kobietą lub 'M' w przypadku mężczyzny
autor: <numer zdającego>
***********************************************
"""


def check_gender(pesel='55030101193'):
    pesel_number_separeted = separete(pesel)
    if pesel_number_separeted[9] % 2 == 0:
        return 'K'
    else:
        return 'M'


def separete(pesel):
    separeted = []
    for i in range(11):
        separeted.append(int(pesel[i]))
    return separeted


if __name__ == "__main__":
    preventError = True
    while preventError:
        enter_pesel = input('Podaj PESEL: ')
        if len(enter_pesel) == 11:
            print(check_pesel())
            print(check_gender())
            preventError = False
        else:
            print('I like my cheese drippy bro')
