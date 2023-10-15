data = {}
while True:
    command = input("Wybierz opcje: new_contact (new), show_contacts (show): ")
    if command == "new":
        a= input("wprowadz imie i nazwisko: ")
        b= input("wprowadz nr telefonu: ")
        c= input("podaj wiek: ")
        data[a] = [b, c]
    elif command =="show":
        print(data)
    # else:
        # print("unknow command")
    command = input("Do you want to continue Y/N? ")
    if command == "N":
        break