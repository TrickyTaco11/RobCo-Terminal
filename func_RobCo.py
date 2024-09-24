from simple_term_menu import TerminalMenu

import termS_RobCo
import cmd_RobCo
import sys_RobCo
import var_RobCo

import time
import os


# Menu's
def return_menu(space, code):
    termS_RobCo.empty()
    cmd_RobCo.char("| returning")
    sys_RobCo.log(space, code, '')
    time.sleep(0.25)
    cmd_RobCo.clear()


def back(space, code):
    option = ["Return"]
    menu = TerminalMenu(option)
    menu_index = menu.show()
    selection = option[menu_index]
    if selection == "Return":
        return_menu(space, code)


def confirm_action(prompt):
    option = ["Yes", "No"]
    menu = TerminalMenu(option, title=prompt)
    choice = menu.show()
    return choice == 0


def exit_info(header):
    cmd_RobCo.char(header.center(var_RobCo.centre, " "))
    print("\n" * 15)
    cmd_RobCo.char(("| RobCoOS " + var_RobCo.softwareV + " |").centre(var_RobCo.centre, " "))
    cmd_RobCo.char("| ⓒ2075 _RobCo |".center(var_RobCo.centre, " "))
    time.sleep(2)
    termS_RobCo.slide_up()


def shutdown():
    if var_RobCo.current_os == "Windows":
        os.system("shutdown /s /t 0")  # Shutdown Windows immediately
    elif var_RobCo.current_os == "Linux" or var_RobCo.current_os == "Darwin":  # Darwin is macOS
        os.system("sudo shutdown -h now")  # Shutdown Linux/macOS
    else:
        cmd_RobCo.char("Shutdown command not supported for this operating system.")


# Entries
def add_entry(directory):
    entry_name = input("Entry name: ").strip()
    if not entry_name:
        print("Entry name cannot be empty.")
        return

    # Remove invalid characters for filenames
    entry_name = "".join([c if c.isalnum() or c in ' ._-' else '_' for c in entry_name])

    filename = os.path.join(directory, f"{entry_name}.txt")
    if os.path.exists(filename):
        if not confirm_action("An entry with this name already exists. Do you want to overwrite it?"):
            print("Entry not saved.")
            return

    entry = input("Enter your entry:\n")

    with open(filename, 'w') as file:
        file.write(entry)

    print(f"Entry saved as {filename}")
    termS_RobCo.empty()


def view_entry(directory):
    entries = os.listdir(directory)
    if not entries:
        print("No entries found.")
        return

    entries_menu = TerminalMenu(entries, title="Select an entry to view")
    choice = entries_menu.show()

    if choice is not None:
        filename = os.path.join(directory, entries[choice])
        with open(filename, 'r') as file:
            cmd_RobCo.char(file.read())
            termS_RobCo.empty()

    else:
        print("No entry selected.")


def clear_entry(directory):
    entries = os.listdir(directory)
    if not entries:
        print("No entries found.")
        return

    entries_menu = TerminalMenu(entries, title="Select an entry to delete")
    choice = entries_menu.show()

    if choice is not None:
        if confirm_action(f"Are you sure you want to delete {entries[choice]}?"):
            filename = os.path.join(directory, entries[choice])
            os.remove(filename)
            print(f"Entry {entries[choice]} deleted.")

    else:
        print("No entry selected.")

    # - - - - - Main System Code(s)

