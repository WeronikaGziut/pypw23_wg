import random

class MyException(Exception):
    pass


def boo():
    if random.random() < 0.5:
        raise Exception("Boo!")
    print("Ok")
try:
    boo()
except MyException:
    print("An exception has occurred")
    print("Trying to safely end the program")
except Exception:
    print("Unknown exception")