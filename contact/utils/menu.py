from contact.utils import (
    add_contact,
    remove_contact,
    get_info_and_update_contact,
    get_input,
    list_contacts,
    search_contact,
    get_contacts,
)
import os
from time import sleep  # Importing sleep function to pause the execution
import inquirer  # Importing inquirer for interactive command line prompts
from colorama import Fore, Style  # Importing colorama for colored terminal output


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")  # Clear


# Function to display the main menu and handle user actions
def menu():
    clear_screen()
    list_contacts(get_contacts())
    while True:
        questions = [
            inquirer.List(
                "action",
                message="Choose Action",
                choices=[
                    "Add",
                    "Delete",
                    "Update",
                    "Search",
                    "List",
                    "Exit (q)",
                ],
            )
        ]
        # Prompt the user to choose an action
        action_response = inquirer.prompt(questions)["action"]

        if action_response == "Add":
            inputs = get_input()
            if inputs:
                add_contact(
                    inputs["name"], inputs["phone"], inputs["email"], inputs["address"]
                )
                clear_screen()
                list_contacts(get_contacts())
                print(Fore.GREEN + "Contact added successfully!" + Style.RESET_ALL)

        elif action_response == "Delete":
            name = input("Enter the name of the contact to delete: ")
            remove_contact(name)
            clear_screen()
            list_contacts(get_contacts())
            print(Fore.GREEN + "Contact deleted successfully!" + Style.RESET_ALL)

        elif action_response == "Update":
            get_info_and_update_contact()
            clear_screen()
            list_contacts(get_contacts())
            print(Fore.GREEN + "Contact updated successfully!" + Style.RESET_ALL)

        elif action_response == "Search":
            clear_screen()
            search_contact()

        elif action_response == "List":
            clear_screen()
            list_contacts(get_contacts())

        elif action_response == "Exit (q)":
            print(Fore.RED + "Exiting..." + Style.RESET_ALL)
            break

        else:
            print(
                Fore.RED
                + "Invalid choice. Please choose a valid option."
                + Style.RESET_ALL
            )
