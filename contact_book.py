contacts = []

def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    # check for duplicate phone or email
    for contact in contacts:
        if contact['phone'] == phone or contact['email'] == email:
            print("Contact with same phone or email already exists.")
            return  # very important!

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
    }

    contacts.append(contact)
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts to display.")
        return
    
    print("\nYour Contacts:")
    for i, contact in enumerate(contacts, 1):
        print(f"\nContact #{i}")
        print(f"Name   : {contact['name']}")
        print(f"Phone  : {contact['phone']}")
        print(f"Email  : {contact['email']}")
        print(f"Address: {contact['address']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\nMatch Found:")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def delete_contact():
    name = input("Enter name of contact to delete: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully.")
            return
    print("Contact not found.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting contact book. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
