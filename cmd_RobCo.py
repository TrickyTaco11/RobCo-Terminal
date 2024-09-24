import sys
import time
import os

import func_RobCo
import termS_RobCo
import sys_RobCo


# Clear screen
clear = lambda: os.system('clear')


# ----- char
def char(userInput):
    for char_ in userInput:
        print(char_, end='')
        sys.stdout.flush()
        time.sleep(0.01)
    print("")


def input_char(userInput):
    for char_ in userInput:
        print(char_, end='')
        sys.stdout.flush()
        time.sleep(0.01)


# ----- read/view/write
def read_specific_line(filename, line_number):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if line_number <= len(lines):
                return lines[line_number - 1].strip()
            else:
                print("Line number exceeds the total number of lines in the file.")
                return None
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def view_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                print(line, end='')
                time.sleep(0.01)
    else:
        char(f"File '{file_path}' does not exist.")


def write_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("")
        char(f"File '{file_path}' successfully cleared")
    else:
        char(f"File '{file_path}' does not exist")


# ----- commands_i
def handle_command(command):
    if command.startswith("view p- "):
        file_path = command[len("view p- "):].strip()
        termS_RobCo.empty()
        view_file(file_path)
        return True
    if command.startswith("clear p- "):
        file_path = command[len("clear p- "):].strip()
        termS_RobCo.empty()
        write_file(file_path)
        sys_RobCo.log(1, 19, "@" + file_path)
        return True
    if command.startswith("print "):
        text_to_print = command[len("print "):].strip()
        termS_RobCo.empty()
        print(text_to_print)
        return True
    if command.startswith("char "):
        termS_RobCo.empty()
        text_to_char = command[len("char "):].strip()
        char(text_to_char)
        return True
    if command.startswith("d=") and "char" in command:
        delay_str = command[len("d="):].split()[0]
        try:
            delay = float(delay_str)  # Convert delay to a float
        except ValueError:
            print("Invalid delay value.")
            return
        text_start_index = command.find("char") + len("char")
        text_to_char = command[text_start_index:].strip()

        # Print each character with delay
        termS_RobCo.empty()
        for char_ in text_to_char:
            print(char_, end='', flush=True)
            time.sleep(delay)
        print()
        return True
    if command == "exit":
        termS_RobCo.empty()
        char("exiting terminal\n")
        time.sleep(2.5)
        termS_RobCo.slide_up()
        exit()
    if command == "restart":
        python = sys.executable
        os.execl(python, python, *sys.argv)
    if command == "shutdown":
        termS_RobCo.empty()
        char("Are you sure you want to shut down the system? (y/n) \n ")
        confirmation = input("!> ")
        if confirmation == "y":
            sys_RobCo.log(1, 12, "shutdown_m")
            func_RobCo.shutdown()
        else:
            termS_RobCo.empty()
            char("Shutdown cancelled")
        return True
    if command == "credits":
        termS_RobCo.credits_()
        return True

    else:
        return False
