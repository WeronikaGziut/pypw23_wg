# file = open("example.txt")
#
# lines = file.readlines()
# for line in lines:
#     #print(line.replace("\n", "")) #print sam dodaje jeden \n
#     print(line, end="")
# print("\n", lines)

# file = open("example.txt", "r")
# for line in file:
#     print(line, end = "")
# file.close()
#nalezy zamykac pliki, mozliwy wyciek file handlerow, moze ona sie wyczerpac
#jesli wydarzy sie na komputerze, trzeba zrestarotwac, tak samo serwer
#serwer baz danych - bardzo zle jesli cos takiego sie stanie

# with open("example.txt", "r") as file:
#     for line in file:
#         print(line, end = "")

#
# def file_lines(file_path):
#     with open(file_path) as file:
#         for line in file:
#             yield line
#
#
# for line in file_lines("example.txt"):
#     print(line)


# file = open("example.txt")
# result = file.readline()
# print(result)
# file.close()
#readline wczytuje linie i przechodzi do nastepnej
# file = open("example.txt")
#
# while result := file.readline():
#     print(result)
# file.close()

#:= do while, operator przypisywania

# file = open("example.txt")
# while result := file.read(10):
#      print(result) #bez argumentow wczytujemy jeden wielki string, liczby to ile bajtow
#
# file.close()

# with open("hello.txt", "w") as file:
#     for _ in range(10):
#         file.write("Hello world\n")
# with open("hello.txt", "w") as file:
#     file.writelines("hello")

# with open("hello.txt", "a") as file:
#     for _ in range(10):
#         print("hello", "Nina", sep=", ", file=file) #dzieki file idzie to do pliku, nie trzeba \n :D

# with open("hello.txt", "r") as file:
#     while result := file.readlines():
#         licznik = {}
#         for i in file:
#             i = i.lower()
#             if i in licznik:
#                 licznik[i] += 1
#             else:
#                 licznik[i] = 1
#         file_1 = open("result1.txt", "w")
#

        # file_1 = open("result.txt", "a")

# import string
# from collections import Counter
#
# def count_letters(in_file, out_file):
#     exclude = {" ", "\n"}.union(set(string.punctuation))
#
#     with open(in_file) as in_file:
#         text = in_file.read()
#
#     c = Counter(text.lower())
#     for letter, freq in c.most_common():
#         if letter not in exclude:
#             with open(out_file, "w") as out_file:
#                 print (letter, freq, file=out_file)
#             break

#
# with open("hello.txt", "w") as file:
#     result = file.read()
#     print(result)
#     print("This is a new line", file=file)

# with open("hello.txt", "w") as file:
#     file.seek(3)
#     file.write("aaaaa!!!")
#
