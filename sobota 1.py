items = [1, 2, 3, 4, 5]
pairs =(x**2 for x in items) #generuje sie generator!!!!!!! specjalna struktura danych
#aby stworzyc tuple, trzeba dodac przed nawiasami tuple
#for a in items:
   # for b in items:
     #   pairs.append((a, b))
#generator nie ma indeksow, jest iterowalny
for pair in pairs:
    print(pair)
for pair in pairs:
    print(pair) #druga petla sie nie wykona ;)
#next zwraca blad, jak juz skoncza nam sie elementy
#next(pairs, None/"No value" itd.) - ustalona wartosc jesli sie skoncza nam elementy
#zeby nauczyc model/sztuczna inteligencje sie przydaje generator, sieci neuronowe
#nie mozemy tu zwierac skomplikowanej logiki, wyrazenie for/if mamy

