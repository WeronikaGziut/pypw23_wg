def words_count(text: str) -> dict:
    slownik = {}
    text = text.lower()
    znak = [".", ","]
    for i in znak:
     text = text.replace(znak, "")
    words = text.split()

    for word in words:

        if word in slownik:
            slownik[word] += 1


        else:
            slownik[word] = 1
    return slownik

result = words_count("Milosz jest Milosz. i nic a nic z tym nie zrobisz")
print(result)

