# Python Essentials 1 SBA
# Contact Book Application


def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()

    if name == "":
        print("Contact name cannot be empty.")
        return

    if name in contacts:
        print("A contact with that name already exists.")
        return

    if not phone.isdigit():
        print("Invalid phone number. Please enter digits only.")
        return

    contacts[name] = phone
    print("Contact added successfully.")


def view_contacts(contacts):
    if len(contacts) == 0:
        print("The contact list is empty.")
        return

    print("\n--- All Contacts ---")

    for name in sorted(contacts):
        print("Name: " + name + " | Phone: " + contacts[name])


def search_contact(contacts):
    search_name = input("Enter a name to search: ").strip().lower()

    found = False

    for name, phone in contacts.items():
        if search_name in name.lower():
            print("Name: " + name + " | Phone: " + phone)
            found = True

    if not found:
        print("No matching contact found.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def display_menu():
    print("\n===== Contact Book Menu =====")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def main():
    contacts = {}

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                add_contact(contacts)

            elif choice == 2:
                view_contacts(contacts)

            elif choice == 3:
                search_contact(contacts)

            elif choice == 4:
                delete_contact(contacts)

            elif choice == 5:
                print("Thank you for using the Contact Book.")
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")


main()