import json
from tabulate import tabulate
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)


# Getting contacts
def get_contacts():
    contacts = []
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
    return contacts


def get_input(name=None, phone=None, email=None):
    contacts = get_contacts()
    if name is None:
        name = input(Fore.GREEN + "Enter name: ")
    for contact in contacts:
        if contact["name"] == name:
            print(Fore.RED + "Contact already exists.")
            return
    if len(name) > 16:
        print(Fore.RED + "Name should be less than 16 characters.")
        return get_input()
    if phone is None:
        phone = input(Fore.GREEN + "Enter phone number: ")
    if len(phone) != 10:
        print(Fore.RED + "Phone number should be 10 digits.")
        return get_input(name=name)
    if email is None:
        email = input(Fore.GREEN + "Enter email: ")
    if "@" not in email or len(email) > 25:
        print(Fore.RED + "Invalid email.")
        return get_input(name=name, phone=phone)
    address = input(Fore.GREEN + "Enter address: ")
    if len(address) > 50:
        print(Fore.RED + "Address too large")
        return get_input(name=name, phone=phone, email=email)
    return {"name": name, "phone": phone, "email": email, "address": address}


# Dumping contacts
def dump_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)


# Adding contact
def add_contact(name, phone, email, address):
    contacts = get_contacts()
    new_contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(new_contact)
    dump_contacts(contacts)


# Removing contact
def remove_contact(name):
    contacts = get_contacts()
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
    dump_contacts(contacts)


# Updating contact
def update_contact(name, phone="", email="", address=""):
    contacts = get_contacts()
    for contact in contacts:
        if contact["name"] == name:
            if phone:
                contact["phone"] = phone
            if email:
                contact["email"] = email
            if address:
                contact["address"] = address
    dump_contacts(contacts)


# Getting update info
def get_info_and_update_contact(name=None):
    if name == None:
        name = input(Fore.GREEN + "Enter name of contact to update: ")
    contacts = get_contacts()
    for contact in contacts:
        if contact["name"] == name:
            phone = input(Fore.GREEN + "Enter New phone (leave blank to skip): ")
            email = input(Fore.GREEN + "Enter New email (leave blank to skip): ")
            address = input(Fore.GREEN + "Enter New address (leave blank to skip): ")
            if phone == "":
                phone = contact["phone"]
            if email == "":
                email = contact["email"]
            if address == "":
                address = contact["address"]
            update_contact(name, phone, email, address)
            return
    print(Fore.RED + "Contact not found.")
    return get_info_and_update_contact()


# List contact using tabulate
def list_contacts(contacts):
    if not contacts:
        print(Fore.RED + "No contacts found.")
        return
    headers = [
        Fore.YELLOW + "Name",
        Fore.YELLOW + "Phone",
        Fore.YELLOW + "Email",
        Fore.YELLOW + "Address",
    ]
    table = []
    for contact in contacts:
        table.append(
            [
                Fore.CYAN + contact["name"],
                Fore.BLUE + contact["phone"],
                Fore.CYAN + contact["email"],
                Fore.BLUE + contact["address"] + Style.RESET_ALL,
            ]
        )
    print(tabulate(table, headers, tablefmt="grid"))
    print(Fore.GREEN + "\nTotal contacts: ", len(contacts), "\n")


# Search contact
def search_contact(name=None):
    temp_contacts = []
    if name == None:
        name = input(Fore.GREEN + "Enter name of contact to search: ")
    contacts = get_contacts()
    for contact in contacts:
        if contact["name"] == name:
            temp_contacts.append(contact)
    if not temp_contacts:
        print(Fore.RED + "Contact not found.")
        return
    list_contacts(temp_contacts)
