import random

"""
************************************************
 nazwa: roll_a_dice
 opis: Program służy do symulacji rzutem kostką. Na początku użytkownik podaje ile ma być rzutów z zakresu 3-10. 
 Następnie wykonuje każdy rzut i go wypisuje. Potem wypisuje liczbe oczek, która wypadła. Potem użytkownik pyta czy chce
 powtórzyć  doświadczenie. Jeżeli kliknie "t" to program wykona ponownie rzuty kostkami. Natomiast jak użytkownik 
 wciśnie "n" to program kończy swoje działanie
 parametry: brak
 zwracany typ i opis: brak, program na bierząco prowadzi dialog z użytkownikiem
 autor: <numer zdającego>
************************************************
"""


def roll_a_dice():
    preventError = True
    while preventError:
        roll_amount = int(input("Ile chce rzucić razu kostką (zakres od 3 do 10 rzutów): "))
        if 3 <= roll_amount <= 10:
            preventError = False
            sum_of_dice = 0
            preventError2 = True
            while preventError2:
                for i in range(roll_amount):
                    roll = random.randint(1, 6)
                    print(f"Kostka {i+1}: {roll}")
                    sum_of_dice += roll
                print("Liczba uzyskanych punktów: ", sum_of_dice)
                preventError3 = True
                while preventError3:
                    again = input("Jeszcze raz? (t/n)\n")
                    if again.lower() == "n":
                        preventError2 = False
                        preventError3 = False
                    elif again.lower() != "t":
                        print("Błąd! (Podaj jeszcze raz)")
                    elif again.lower() == "t":
                        preventError3 = False
        else:
            print("Błąd")


if __name__ == "__main__":
    roll_a_dice()
