import random
from INF_04_02_23_06_SG import bubble_sort


def test_bubble_sort():
    array_to_sort = [random.randint(0, 1000) for _ in range(100)]
    print("Przed sortowaniem:", array_to_sort)
    bubble_sort(array_to_sort)
    print("Po sortowaniu:   ", array_to_sort)


if __name__ == "__main__":
    test_bubble_sort()
