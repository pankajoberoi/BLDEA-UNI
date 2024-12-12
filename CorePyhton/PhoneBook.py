# phonebook.py
def display_menu():
    print("\nPhonebook Menu")
    print("1. Add a New Contact")
    print("2. Search for a Contact")
    print("3. Delete a Contact")
    print("4. List All Contacts")
    print("5. Exit")


def add_contact(phonebook):
    name = input("Enter contact name: ").strip()
    if name in phonebook:
        print(f"{name} already exists in the phonebook with number {phonebook[name]}.")
    else:
        phone = input("Enter phone number: ").strip()
        phonebook[name] = phone
        print(f"Contact {name} added successfully.")


def search_contact(phonebook):
    name = input("Enter the name to search: ").strip()
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}.")
    else:
        print(f"Contact {name} not found in the phonebook.")


def delete_contact(phonebook):
    name = input("Enter the name to delete: ").strip()
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found in the phonebook.")


def list_contacts(phonebook):
    if not phonebook:
        print("The phonebook is empty.")
    else:
        print("\nPhonebook Contacts:")
        for name, phone in phonebook.items():
            print(f"Name: {name}, Phone: {phone}")


# Main function to execute the program
def main():
    phonebook = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            search_contact(phonebook)
        elif choice == "3":
            delete_contact(phonebook)
        elif choice == "4":
            list_contacts(phonebook)
        elif choice == "5":
            print("Exiting the Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

# Direct execution of main() without the `if __name__ == "__main__":` construct
main()
