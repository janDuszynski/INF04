# Ciąg Fibonacciego: iteracyjnie O(n), rekurencyjnie O(2^n)
def fibonacci_iteracyjnie(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_rekurencyjnie(n):
    if n < 2:
        return n
    return fibonacci_rekurencyjnie(n - 1) + fibonacci_rekurencyjnie(n - 2)


if __name__ == "__main__":
    print("Pierwsze 15 wyrazów (iteracyjnie):")
    for n in range(15):
        print(fibonacci_iteracyjnie(n), end=" ")
    print()
    print("Pierwsze 15 wyrazów (rekurencyjnie):")
    for n in range(15):
        print(fibonacci_rekurencyjnie(n), end=" ")
    print()
