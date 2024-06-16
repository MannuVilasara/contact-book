import argparse
import sys
from contact.utils import (
    get_input,
    get_contacts,
    list_contacts,
    add_contact,
    get_info_and_update_contact,
    remove_contact,
    menu,
    search_contact,
)
from colorama import Fore, Style


def main():
    parser = argparse.ArgumentParser(description="A Contact Book written in python")
    parser.add_argument("--add", help="Add new contact")
    parser.add_argument("--delete", help="Delete a contact")
    parser.add_argument("--search", help="Search for a contact")
    parser.add_argument("--update", help="Update Contact")
    parser.add_argument("--list", help="List all contacts", action="store_true")

    args = parser.parse_args()
    provided_args = sum(arg is not None for arg in vars(args).values())

    # Ensure only one argument is provided at a time
    if provided_args > 2:
        print("Error: Only one argument can be passed at a time.")
        sys.exit(1)

    if args.add:
        inputs = get_input(args.add)
        if inputs:
            add_contact(
                inputs["name"], inputs["phone"], inputs["email"], inputs["address"]
            )
            print(Fore.GREEN + "Contact added successfully!" + Style.RESET_ALL)
    elif args.delete:
        remove_contact(args.delete)
        print(Fore.RED + "Contact deleted successfully!" + Style.RESET_ALL)
    elif args.search:
        search_contact(args.search)
    elif args.update:
        get_info_and_update_contact(args.update)
        print(Fore.GREEN + "Contact updated successfully!" + Style.RESET_ALL)

    elif args.list:
        contacts = get_contacts()
        list_contacts(contacts)
    else:
        menu()


if __name__ == "__main__":
    main()
