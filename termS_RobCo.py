import os
import time
import sys

import sys_RobCo
import var_RobCo
import cmd_RobCo


# ----- headers
def header_(header_input, centre_input, typeF):
    empty()
    line()
    typeF((" " + header_input + " ").center(var_RobCo.centre, centre_input))
    line()
    empty()


# ----- cheats
def empty():
    print("")  # Creates an empty space in the display


def line():
    print('--'.center(var_RobCo.centre, '-'))  # Creates a line going across the screen


# ----- effects
def load_wheel(timeNumber):
    loadWheelAnimation = ".", ". .", ". . .", ". . . ."

    for i in range(timeNumber):
        time.sleep(0.1)
        sys.stdout.write("\rLOADING: " + loadWheelAnimation[i % len(loadWheelAnimation)])
        sys.stdout.flush()


def robco_interface(typeF):
    cmd_RobCo.clear()
    empty()

    typeF("ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM".center(var_RobCo.centre, " "))
    typeF("COPYRIGHT 2075-2077 ROBCO INDUSTRIES".center(var_RobCo.centre, " "))
    with open(var_RobCo.server, 'r') as f:
        typeF(f.read().center(var_RobCo.centre, " "))
    print(" \n" * 3)


def logo_screen(number):
    print("\n" * number)
    print("██████|  █████| ██████|  █████|  █████| ".center(var_RobCo.centre, " "))
    print("██|  ██|██|  ██|██|  ██|██|  ██|██|  ██|".center(var_RobCo.centre, " "))
    print("██████| ██|  ██|██████| ██|     ██|  ██|".center(var_RobCo.centre, " "))
    print("██|  ██|██|  ██|██|  ██|██|  ██|██|  ██|".center(var_RobCo.centre, " "))
    print("██|  ██| █████| ██████|  █████|  █████| ".center(var_RobCo.centre, " "))
    print("\n" * number)


def print_s(text, speed):
    for line_section in text.split('\n'):
        print(line_section)
        time.sleep(speed)


def slide_by_line(filename, delay):
    with open(filename, 'r') as file:
        for line1 in file:
            print(line1, end='')
            time.sleep(delay)


def slide_up():
    for i in range(30):
        print("")
        time.sleep(0.02)
    cmd_RobCo.clear()


def locate_file_screen():
    def find_item(path_file):
        cmd_RobCo.clear()
        logo_screen(11)
        if os.path.exists(path_file):
            if os.path.isfile(path_file):
                return " > file_located"
            elif os.path.isdir(path_file):
                return " > dir_located"
        else:
            sys_RobCo.m_log(86, f"missing:{path_file}")
            return " >>>>> ERROR: NOT FOUND <<<<<"

    for path in var_RobCo.paths:
        status = find_item(path)
        print(f"Loading: {path}: {status}")

    logo_screen(11)


def credits_():
    empty()
    cmd_RobCo.char("Created by TrickyTaco11 @2024 \nThanks to Bethesda Softworks "
                   "for inspiration on the Fallout styled RobCo-Terminal! \n"
                   "Licensed by MIT \n"
                   "https://github.com/TrickyTaco11/RobCo-Terminal \n ")
