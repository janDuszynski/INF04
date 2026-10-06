import random


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


if __name__ == "__main__":
    array_to_sort = [random.randint(-100, 100) for i in range(100)]
    print(array_to_sort)
    bubble_sort(array_to_sort)
    print(array_to_sort)
