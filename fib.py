# def fib(n):
#     if n < 0:
#         return "Błąd: n musi być liczbą całkowitą większą od 0"
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a = 0
#         b = 1
#         for _ in range(n - 2):
#             a = b
#             b = a + b
#         return b
#
# n = int(input("Wprowadz, dla ktorego elementu ciagu Fib chcesz poznac wartosc: "))
# wynik = fib(n)
# print(f"{n}-ty element ciągu Fibonacciego to: {wynik}")

_cache = {}


def fib_rek(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    if n not in _cache:
        _cache[n] = fib_rek(n-1) + fib_rek(n-2)
    return _cache[n]



n = int(input("wprowadz element ciagu Fib: "))
print(fib_rek(n))