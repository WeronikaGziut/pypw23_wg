a = []

a.append(42) #append to tak naprawde metoda klasy

class Car:
#self to argument ktory zawsze jest, pierwszy, tylko w deklaracji metody
#to wskaznik na obiekt klasy/instancje
    def __init__(self, registration_number): #konstruktor, poczatkowe ustawienia
        self.registration_number = registration_number
        self.speed = 0

    def drive(self):
        self.speed += 10

    def __repr__(self):
        return f"Car ({self.registration_number})"

car = Car("WAW-17236") #odpalamy init
car.drive()
print(car)











