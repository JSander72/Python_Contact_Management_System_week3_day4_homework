import re
import json

contacts = {}

def display_menu():
    print("""
    Welcome to the Contact Management System!
    Please choose an option:
    1. Add a new contact
    2. Edit an existing contact
    3. Delete a contact
    4. Search for a contact
    5. Display all contacts
    6. Export contacts to a text file
    7. Import contacts from a text file
    8. Quit
    """)

def add_contact():
    print("Adding a new contact")
    email = input("Enter email (unique identifier): ")
    if email in contacts:
        print("A contact with this email already exists.")
        return
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    additional_info = input("Enter additional information: ")
    
    # Validate inputs using regex
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format.")
        return
    if not re.match(r"^\+?[1-9]\d{1,14}$", phone):
        print("Invalid phone number format.")
        return
    
    contacts[email] = {
        "name": name,
        "phone": phone,
        "additional_info": additional_info
    }
    print("Contact added successfully!")

def edit_contact():
    print("Editing an existing contact")
    email = input("Enter the email of the contact to edit: ")
    if email not in contacts:
        print("No contact found with this email.")
        return
    name = input("Enter new name: ")
    phone = input("Enter new phone number: ")
    additional_info = input("Enter new additional information: ")
    
    # Validate inputs using regex
    if not re.match(r"^\+?[1-9]\d{1,14}$", phone):
        print("Invalid phone number format.")
        return

    contacts[email].update({
        "name": name,
        "phone": phone,
        "additional_info": additional_info
    })
    print("Contact updated successfully!")

def delete_contact():
    print("Deleting a contact")
    email = input("Enter the email of the contact to delete: ")
    if email in contacts:
        del contacts[email]
        print("Contact deleted successfully!")
    else:
        print("No contact found with this email.")

def search_contact():
    print("Searching for a contact")
    email = input("Enter the email of the contact to search: ")
    if email in contacts:
        print(f"Details for {email}: {contacts[email]}")
    else:
        print("No contact found with this email.")

def display_all_contacts():
    print("Displaying all contacts")
    for email, details in contacts.items():
        print(f"{email}: {details}")

def export_contacts():
    print("Exporting contacts to a text file")
    with open("contacts.txt", "w") as file:
        file.write(json.dumps(contacts, indent=4))
    print("Contacts exported successfully!")

def import_contacts():
    print("Importing contacts from a text file")
    try:
        with open("contacts.txt", "r") as file:
            imported_contacts = json.load(file)
            contacts.update(imported_contacts)
        print("Contacts imported successfully!")
    except FileNotFoundError:
        print("No such file found.")
    except json.JSONDecodeError:
        print("Error decoding the file content.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            display_all_contacts()
        elif choice == "6":
            export_contacts()
        elif choice == "7":
            import_contacts()
        elif choice == "8":
            print("Quitting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
