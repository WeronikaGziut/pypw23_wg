from string import punctuation
from collections import defaultdict

def words_count(text: str) -> dict:
    slownik = defaultdict(int)
    text = text.lower()
    for char in punctuation:
        text = text.replace(char, "")
    words = text.split()

    for word in words:
        slownik[word] += 1

    return slownik

result = words_count("Milosz, jest Milosz. i nic a nic z tym nie# zrobisz")
print(result)

