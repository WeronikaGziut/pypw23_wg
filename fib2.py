def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a #zwracamy a i idziemy dalej
        a, b = b, a + b
#to jest generator


#yield jak python spotka, to wyrzuci co z fukncji, ale bkontynuowal dzialanie

i = 0
for n in fib(10):
    print(i, n)
    i += 1

print(list(fib(10)))
# def fib_items(n):
#     return (fib(x) for x in range(n))
# print(fib_items(10))