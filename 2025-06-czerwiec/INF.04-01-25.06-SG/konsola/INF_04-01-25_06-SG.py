import random

"""
************************************************
 nazwa funkcji: fill_draws
 opis funkcji: losuje podaną liczbę zestawów po sześć różnych liczb całkowitych z zakresu 1-49
 parametry: draws_amount - liczba zestawów do wylosowania
 zwracany typ i opis: list - dwuwymiarowa lista (draws_amount wierszy i 6 kolumn) z wylosowanymi liczbami
 autor: <numer zdającego>
************************************************
"""


def fill_draws(draws_amount):
    draws = []
    for i in range(draws_amount):
        draws.append(random.sample(range(1, 50), 6))
    return draws


def print_draws(draws):
    print("Zestawy wylosowanych liczb:")
    for i in range(len(draws)):
        numbers = " ".join(str(number) for number in draws[i])
        print(f"Losowanie {i + 1}: {numbers}")


def count_numbers(draws):
    counts = [0] * 50
    for draw in draws:
        for number in draw:
            counts[number] += 1
    return counts


def print_counts(counts):
    for number in range(1, 50):
        print(f"Wystąpienia liczby {number}: {counts[number]}")


def main():
    draws_amount = int(input("Ile wygenerować losowań?\n"))
    draws = fill_draws(draws_amount)
    print_draws(draws)
    counts = count_numbers(draws)
    print_counts(counts)


if __name__ == "__main__":
    main()
