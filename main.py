def read_phone_numbers():
    phonebook = {}
    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook
def print_phonebook(phonebook):
    print("\n--- Phonebook ---")
    for name, number in phonebook.items():
    
        print(name + " -> " + number)
    print("-----------------\n")
def lookup_numbers(phonebook):
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break

        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print("Number:", phonebook[name])
def update_number(phonebook):
    name = input("Enter name to update: ")

    if name == "":
        print("Update cancelled.")
        return

    if name not in phonebook:
        print(name + " is not in the phonebook.")
        return
    
    new_number = input("Enter new number: ")
    phonebook[name] = new_number
    print("Updated", name, "to", new_number)
def delete_number(phonebook):
    name = input("Enter name to delete: ")

    if name == "":
        print("Delete cancelled.")
        return
    
    if name not in phonebook:
        print(name + " is not in the phonebook.")
        return

    del phonebook[name]
    print(name, "has been deleted.")
phonebook = read_phone_numbers()

while True:
    print("\nMENU")
    print("1. Show phonebook")
    print("2. Lookup number")
    print("3. Update number")
    print("4. Delete number")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print_phonebook(phonebook)
    elif choice == "2":
        lookup_numbers(phonebook)
    elif choice == "3":
        update_number(phonebook)
    elif choice == "4":
        delete_number(phonebook)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")