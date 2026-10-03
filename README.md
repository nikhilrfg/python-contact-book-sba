# Python Essentials 1 SBA - Contact Book

## Description

This project is a console-based Contact Book application created for the
Python Essentials 1 SBA.

The application allows users to:

- Add new contacts
- View all contacts
- Search for contacts
- Delete contacts
- Exit the application

## Program Structure

The program uses a Python dictionary to store contacts. The contact name
is used as the dictionary key and the phone number is stored as the value.

The program contains the following functions:

- `add_contact()` - Adds a new contact and prevents duplicate names.
- `view_contacts()` - Displays all contacts alphabetically.
- `search_contact()` - Searches for a contact by full or partial name.
- `delete_contact()` - Removes a contact from the dictionary.
- `display_menu()` - Displays the Contact Book menu.
- `main()` - Controls the main program loop.

## Input Validation

The program checks for:

- Duplicate contact names
- Empty contact names
- Invalid phone numbers
- Invalid menu choices
- Non-numeric menu input

A `try/except` block is used to handle invalid menu input.

## Challenges

One challenge was making sure duplicate contacts were not added to the
dictionary. I solved this by checking whether the contact name already
exists before adding it.

Another challenge was handling invalid menu input without crashing the
program. I used a `try/except` block to catch `ValueError`.

## Concepts Used

This project demonstrates:

- Variables
- Input and output
- Conditionals
- While loops
- For loops
- Functions
- Dictionaries
- String methods
- Exception handling