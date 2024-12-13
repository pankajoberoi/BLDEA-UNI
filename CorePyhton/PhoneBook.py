#PhoneBook
def display_menu():
    print("\nPhoneBook Menu")
    print("1.Add a new Conatct")
    print("2.Search for a Contact")
    print("3.Update a Contact's Phone number")
    print("4.Delete a Contact")
    print("5.List of All contacts ")
    print("6.Exit")
    

def add_contact(phonebook):
    name=input("Enter the contact name: ")
    if name in phonebook:
        print(f"{name} already exists!! in you phonebook with number {phonebook[name]}")
    else:
        phone=input("Enter Phone number ") 
        phonebook[name]=phone   
        print(f"Contact {name} added successfully")

def search_contact(phonebook):
    name=input("Enter the name to search")
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}")
    else:
        print(f"Contact {name} not found in the phonebook")
        
def update_contact(phonebook):
    name=input("Enter the name of the contact you want to update: ")
    
    if name in phonebook:
        new_phone=input(f"Enter the new phone number for {name}")
        phonebook[name]=new_phone
        print(f"{name}'s phone number is updated succesfully.")
    
    else:
        print(f"Contact {name} not found in your PhoneBook")    
    
def delete_contact(phonebook):
    name=input("Enter the name to delete ")
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} has been deleted succesfully!!")
    
    else:
        print(f"Contact {name} not found in your phonebook!")
    

def list_contact(phonebook):
    if not phonebook:
        print("the phoneBook is empty.")
    else:
        print("\nPhonebook Contact: ")
        for name,phone in phonebook.items():
            print(f"Name : {name}, Phone : {phone}")
        
    

def main():
    
    phonebook={}
    while(True):
        display_menu()
        choice=input("Enter Your Choice")
        
        if choice == "1":
            add_contact(phonebook)

        elif choice == "2":
            search_contact(phonebook)
            
        elif choice == "3":
            update_contact(phonebook)
            
        elif choice == "4":
            delete_contact(phonebook)
            
        elif choice == "5":
            list_contact(phonebook)
            
        elif choice == "6":
            print("Exiting the phonebook . Goodbye!")
            break
        
        else:
            print("Abbe andha hai kya!!!")


main()