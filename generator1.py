# def evens(n):
#     for x in range(2*(n)):
#         if x % 2 == 0:
#             yield x
#
# n = int(input("podaj n: "))
# print(list(evens(n)))

def prime(n: int) -> bool:
    if n == 0 or n == 1:
       return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# n = int(input("podaj n: "))
# print((prime(n)))

def prime_gen(num):
    count = 0
    p = 2
    while count < num:
        if prime(p):
            yield p
            count += 1
        p += 1
num = int(input("ile chcesz liczb pierwszych? "))
# for p in prime_gen(10):
#     print(p)

print(list(prime_gen(num)))




