import time
from time import sleep


def timeit(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"Duration: {end - start}")
        return result
    return wrapper #zwracamy funkcje, a nie to, co funkcja zwraca
#opakowanie robi co przed wywolaniem funkcji i po
#parametry wrapper takie same jak greeting

@timeit
def greeting():
    print("hello world")
    sleep(3)

#greering = timeit(greeting)

greeting()

#*args dowolna ilosc pozycyjnych argumentow * tuple
#*kwargs (nie musimy to pisac, istotne gwiazdki) dowolona ilosc nazwanych argumentow ** slownik
@timeit
def div(a,b):
    c = a / b
    print(c)
div(6,2)