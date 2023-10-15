import json
from pathlib import Path

path = Path("data.json")

if path.exists():
    f = open(path, "r")
    data = json.load(f)
    f.close()
else:
    data = {}

commands = ["new_contact", "show_contacts"]
while True:
    command = input(f"Wybierz opcje: {commands} ")
    while command not in commands:
        print("Unknown command, try again: ")
        command = input(f"Wybierz opcje: {commands} ")
    if command == "new_contact":
        a= input("wprowadz imie i nazwisko: ")
        b= input("wprowadz nr telefonu: ")
        data[a] = [b]
    elif command =="show_contacts":
        print(data)
    answer = input("Do you want to continue Y/N? ")
    while answer.lower() not in ["y", "n"]:
        print("Choose Y or N only")
        answer = input("Do you want to continue Y/N? ")
    if answer.lower() == "n":
        f = open("data.json", "w")
        json.dump(data, f)
        f.close()
        break