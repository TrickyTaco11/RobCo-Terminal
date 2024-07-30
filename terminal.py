#
#
#
#
# Based from Fallout 3 and 4's terminal system while taking inspiration from old CRT terminals from the 80's.
# This project is designed to run in terminal or a terminal emulator, preferably in 'cool-retro-term'.
#
#
#
#
# ---------- Imports ----------
from simple_term_menu import TerminalMenu
from getpass import getpass
from datetime import *

import subprocess
import platform
import logging
import shutil
import socket
import random
import string
import bcrypt
import getch
import time
import sys
import os

#
#
#
#
# ---------- Variables ----------
# Date and time
today = date.today()
current = datetime.now()

year = today.strftime("%Y")
currentDate = today.strftime("%d/%m/%Y")
currentTime = current.strftime('%H:%M:%S')

# User txt
UserTXT = "user_info/user.txt"
PasswordTXT = "user_info/password.txt"
credTXT = "user_info/credential.txt"
clearanceTXT = "user_info/clearance.txt"

# Security txt
securitylvlTXT = "security_level/security-level.txt"
securityrlvlTXT = "security_level/security-level-reasoning.txt"
systemLogLOG = "system/system-logs.log"

# Other txt
msis = "system/msis.txt"

# Reading txt
with open(UserTXT, "r") as userFile:
    user = userFile.readline().strip("\n")

with open("user_info/password.txt", "rb") as file:
    encrypted_password_from_file = file.read()

with open(credTXT, "r") as credFile:
    credential = credFile.readline().strip("\n")

with open(clearanceTXT, "r") as clearanceFile:
    clearance = clearanceFile.readline().strip("\n")

with open(securitylvlTXT, "r") as securityLvlFile:
    securityLevel = securityLvlFile.readline().strip("\n")

with open(securityrlvlTXT, "r") as securityLvlRRFile:
    securityLvlRR = securityLvlRRFile.readline().strip("\n")

# Directories
userInfo_dir = "user_info"
os.makedirs(userInfo_dir, exist_ok=True)

journal_dir = "journal_entries"
os.makedirs(journal_dir, exist_ok=True)

archive_dir = "archive_entries"
os.makedirs(archive_dir, exist_ok=True)

security_dir = "security_logs"
os.makedirs(security_dir, exist_ok=True)

protocols_dir = "security_protocols"
os.makedirs(protocols_dir, exist_ok=True)

securityLevel_dir = "security_level"
os.makedirs(securityLevel_dir, exist_ok=True)

emergencyProtocol_dir = "emergency_protocols"
os.makedirs(emergencyProtocol_dir, exist_ok=True)

error_dir = "error_codes"
os.makedirs(error_dir, exist_ok=True)

system_dir = "system"
os.makedirs(system_dir, exist_ok=True)

backup_dir = "backup_data"
os.makedirs(backup_dir, exist_ok=True)

# Paths
paths = [
    'archive_entries',
    'emergency_protocols',
    'error_codes',
    'journal_entries',
    'security_level',
    'security_logs',
    'security_protocols',
    'venv',
    'user_info/clearance.txt',
    'system/corrupt-error.txt',
    'user_info/credential.txt',
    'system/help-menu.txt',
    'system/msis.txt',
    'user_info/password.txt',
    'security_level/security-level.txt',
    'security_level/security-level-reasoning.txt',
    'system/sevenletterwords.txt',
    'system/server-system.txt',
    'system/system-logs.log',
    'user_info/user.txt',
    'terminal.py',
]
directoryB_paths = ["archive_entries", "emergency_protocols", "error_codes", "journal_entries", "security_level",
                    "security_logs", "security_logs", "security_protocols", "system", "user_info", "venv"]

# Settings
centre = 95
progressI = "- IN PROGRESS - ".center(centre, "-")

# System
clear = lambda: os.system('clear')
softwareV = "v4.1"
server = "system/server-system.txt"
backup_location = backup_dir

# SALLI
salliV = "v2.7"
salliY = "2020-" + year
ai = "ⓒ" + year + " SALLI"
fullAI = "ⓒ" + salliY + " SALLI " + salliV

# Internet
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)

# Encryption


# Chars
GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'


#
#
#
#
# ---------- Define ----------
# Functions
def empty():
    print("")


def line():
    print("--".center(centre, '-'))


def back(space, code):
    returnOption = ["Return"]
    menu_return = TerminalMenu(returnOption)
    return_index = menu_return.show()
    returnSelection = returnOption[return_index]
    if returnSelection == "Return":
        return_menu(space, code)


def charp(userInput):
    for charP in userInput:
        print(charP, end='')
        sys.stdout.flush()
        time.sleep(0.01)


def input_char(userInput):
    for charI in userInput:
        print(charI, end='')
        sys.stdout.flush()
        time.sleep(0.01)


def return_menu(space, code):
    empty()

    charp("| returning")
    sys_log2(space, code, '')
    time.sleep(0.25)

    clear()


def header_charp(header_input, centre_input):
    empty()

    line()
    charp(("-- " + header_input + " --").center(centre, centre_input))
    line()

    empty()


def header_print(header_input, centre_input):
    empty()

    line()
    print(("-- " + header_input + " --").center(centre, centre_input))
    line()

    empty()


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


def exit_info(header):
    charp(header.center(centre, " "))
    empty()

    print("\n" * 14)
    charp(("| RobCoOS " + softwareV + "|").center(centre, " "))
    charp(("| ⓒ" + year + " RobCo |").center(centre, " "))
    time.sleep(2)
    slide_up()


def confirm_action(prompt):
    options = ["Yes", "No"]
    menu = TerminalMenu(options, title=prompt)
    choice = menu.show()
    return choice == 0


def handle_command(command):
    if command.startswith("view d- "):
        try:
            _, _, directory, filename = command.split(' ', 3)
            file_path = os.path.join(directory, filename)
            view_file(file_path)
        except ValueError:
            charp("Invalid command format. Use: view d- {directory} {filename}")

    if command.startswith("view f- "):
        try:
            _, _, filename = command.split(' ', 2)
            file_path = filename
            view_file(file_path)
        except ValueError:
            charp("Invalid command format. Use: view f- {filename}")

    if command.startswith(f"view p- "):
        file_path = command[len("view p- "):].strip()
        view_file(file_path)


def view_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line1 in file:
                print(line1, end='')
                time.sleep(0.01)
    else:
        charp(f"File {file_path} does not exist.")


def set_test_message():
    print("This is a test message to showcase the current text and background colour. > !@#123ABCabc <")


# Encryption
def encrypt_user(y):
    return ''.join(
        random.choice(string.ascii_letters + string.digits + string.punctuation + string.hexdigits + string.octdigits)
        for _ in range(y))


def encoded_input(message):
    print(message, end='')
    pw = ""
    while True:
        symbol = getch.getch()
        if symbol == "\n" or symbol == "\r":
            break
        print("*", end="", flush=True)
        pw += symbol
    print()
    return pw


# locate files
def locate_file_screen():
    def find_item(path_file):
        clear()

        logo_screen(11)

        if os.path.exists(path_file):
            if os.path.isfile(path_file):
                return "File found"
            elif os.path.isdir(path_file):
                return "Directory found"
        else:
            return "Error: Not found"

    for path in paths:
        status = find_item(path)
        print(f"Loading: {path}: {status}")

    logo_screen(11)


#
#
# System
# - - - Status
def get_system_status():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    network_info = get_network_info()
    cpu_temp = get_cpu_temperature()

    return {
        "CPU": {"status": "OK", "usage": f"{cpu_usage}%",
                "temperature": f"{cpu_temp}°C" if cpu_temp is not None else "N/A"},
        "MEMORY": {"status": "OK", "usage": f"{memory_usage}%", "available": "N/A"},
        "HARD DRIVE": {"status": "OK" if disk_usage['percent'] < 90 else "WARNING",
                       "disk space": "LOW" if disk_usage['percent'] > 90 else "OK", "errors detected": "N/A",
                       "total space": f"{disk_usage['total']} GB", "free space": f"{disk_usage['free']} GB"},
        "NETWORK": {"status": "OK" if network_info else "N/A", "connection": "Stable", "signal strength": "N/A"},
        "POWER SUPPLY": {"status": "N/A", "voltage": "N/A", "current": "N/A"}
    }


def display_system_status(status):
    lines = []
    empty()

    lines.append("- SYSTEM DIAGNOSTIC REPORT -".center(centre, "-"))
    empty()

    lines.append(f"--".center(centre, "-"))
    lines.append(f"[INFO] SYSTEM STATUS: ONLINE")
    lines.append(f"[INFO] LAST SYSTEM CHECK: {time.strftime('%H:%M:%S')}")
    lines.append(f"[INFO] CURRENT USER: {platform.node()} | " + currentUser)
    lines.append(f"--".center(centre, "-"))

    lines.append("- COMPONENT STATUS -".center(centre, "-"))
    for component, info in status.items():
        lines.append(f"{component}: {info['status']}")
        for key, value in info.items():
            if key != 'status':
                lines.append(f"   - {key}: {value}")
        lines.append("")
    print_slowly('\n'.join(lines))


# - - - Reports
def main_system_diagnostics_report():
    status = get_system_status()
    errors = get_error_log()

    display_system_status(status)
    display_error_log(errors)
    display_recommendations()


def view_system_performance_report():
    print("\n[INFO] Viewing system performance report...")
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")


# - - - CPU
def get_cpu_usage():
    try:
        if platform.system() == 'Linux':
            result = subprocess.run(['top', '-bn1'], capture_output=True, text=True)
            for sys_line in result.stdout.splitlines():
                if "Cpu(s)" in sys_line:
                    return sys_line.split('%Cpu(s):')[1].split(',')[0].strip()
        elif platform.system() == 'Darwin':
            result = subprocess.run(['top', '-l1'], capture_output=True, text=True)
            for sys_line in result.stdout.splitlines():
                if "CPU usage" in sys_line:
                    return sys_line.split(' ')[-3].strip()
        return "N/A"
    except Exception as e:
        return f"Error: {e}"


def get_cpu_temperature():
    try:
        if platform.system() == 'Linux':
            with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
                temp = int(file.read().strip()) / 1000
                return temp
        elif platform.system() == 'Darwin':
            result = subprocess.run(['osx-cpu-temp'], capture_output=True, text=True)
            temp = result.stdout.strip().split('°')[0]
            return float(temp) if temp else None
        else:
            return None
    except Exception:
        return None


# - - - Memory
def get_memory_usage():
    try:
        if platform.system() == 'Linux':
            result = subprocess.run(['free', '-m'], capture_output=True, text=True)
            lines = result.stdout.splitlines()
            memory_line = lines[1].split()
            used_memory = int(memory_line[2])
            total_memory = int(memory_line[1])
            return round((used_memory / total_memory) * 100, 2)
        elif platform.system() == 'Darwin':
            result = subprocess.run(['vm_stat'], capture_output=True, text=True)
            vm_stats = result.stdout.splitlines()
            total_memory = int(vm_stats[1].split(':')[1].strip().replace('.', ''))
            free_memory = int(vm_stats[5].split(':')[1].strip().replace('.', ''))
            used_memory = total_memory - free_memory
            return round((used_memory / total_memory) * 100, 2)
        return "N/A"
    except Exception as e:
        return f"Error: {e}"


# - - - Disk
def get_disk_usage():
    try:
        if platform.system() in ['Linux', 'Darwin']:
            result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
            lines = result.stdout.splitlines()
            if len(lines) > 1:
                parts = lines[1].split()
                return {
                    'total': parts[1],
                    'used': parts[2],
                    'free': parts[3],
                    'percent': int(parts[4].replace('%', ''))
                }
        return {'total': 'N/A', 'used': 'N/A', 'free': 'N/A', 'percent': 0}
    except Exception as e:
        return {'total': 'N/A', 'used': 'N/A', 'free': 'N/A', 'percent': 0}


# - - - Network
def get_network_info():
    try:
        if platform.system() == 'Linux':
            result = subprocess.run(['ifconfig'], capture_output=True, text=True)
            return result.stdout
        elif platform.system() == 'Darwin':
            result = subprocess.run(['ifconfig'], capture_output=True, text=True)
            return result.stdout
        return "N/A"
    except Exception as e:
        return f"Error: {e}"


# - - - Error
def get_error_log():
    log_entries = []
    log_files = ['/var/log/syslog', '/var/log/messages']

    for log_file in log_files:
        if os.path.exists(log_file):
            try:
                with open(log_file, 'r') as file:
                    lines = file.readlines()[-10:]  # Read the last 10 lines for brevity
                    log_entries.extend([f"[{time.strftime('%H:%M:%S')}] {line.strip()}" for line in lines])
            except Exception as e:
                log_entries.append(f"[ERROR] Unable to read {log_file}: {str(e)}")

    return log_entries


def display_error_log(errors):
    lines = ["- ERROR LOG -".center(centre, "-")]
    if errors:
        for error in errors:
            lines.append(error)
    else:
        lines.append("[INFO] No errors found.")
    lines.append("")
    print_slowly('\n'.join(lines))


# - - - Recommendations
def display_recommendations():
    lines = ["- SYSTEM RECOMMENDATIONS -".center(centre, "-")]
    recommendations = [
        "1. Clear unnecessary files to free up disk space.",
        "2. Run disk repair utility to fix read/write errors.",
        "3. Ensure proper ventilation for CPU to avoid overheating.",
        "4. Check network connections and stability to prevent packet loss.",
        "5. Review system logs for potential security threats."
    ]
    for recommendation in recommendations:
        lines.append(recommendation)
    lines.append("")
    print_slowly('\n'.join(lines))


# - - - Updates
def check_for_updates():
    os_name = platform.system()
    if os_name == 'Linux':
        try:
            result = subprocess.run(["apt-get", "update"], capture_output=True, text=True)
            print("\n[INFO] Checking for updates...")
            print(result.stdout)
        except Exception as e:
            print(f"[ERROR] Failed to check for updates: {e}")
    elif os_name == 'Darwin':
        try:
            result = subprocess.run(["brew", "update"], capture_output=True, text=True)
            print("\n[INFO] Checking for updates...")
            print(result.stdout)
        except Exception as e:
            print(f"[ERROR] Failed to check for updates: {e}")
    else:
        print("\n[ERROR] Unsupported operating system for update checking.")


# - - - Backup
def backup_data(directories, backup_path):
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)

    for directory in directories:
        if os.path.exists(directory):
            dest = os.path.join(backup_path, os.path.basename(directory))
            if os.path.exists(dest):
                shutil.rmtree(dest)
            shutil.copytree(directory, dest)
            print(f"Backed up {directory} to {dest}")
        else:
            print(f"Directory {directory} does not exist")


# - - - Reboot
def reboot_system():
    os_name = platform.system()
    if os_name in ['Linux', 'Darwin']:
        print("\n[INFO] Rebooting system...")
        time.sleep(1)
        os.system("sudo reboot")
    else:
        print("\n[ERROR] Unsupported operating system for reboot.")


# System logs
logging.basicConfig(
    filename='system/system-logs.log',  # Log file name
    level=logging.INFO,  # Log level
    format='%(asctime)s - %(message)s',  # Log format with timestamp
    datefmt='%Y-%m-%d %H:%M:%S'  # Date and time format
)


def sys_log(code_number, if_input):
    logging.info("* $RobCo_OS:  system:" + read_specific_line("system/system-codes-for-log.txt", code_number)
                 + if_input)


def sys_log2(space_number, code_number, if_input):
    space = "   " * space_number + "* "
    logging.info("* $RobCo_OS:  system:" + space + read_specific_line("system/system-codes-for-log.txt", code_number)
                 + if_input)


def sys_logEmpty():
    with open(systemLogLOG, 'a') as F:
        F.write(" \n")
    with open(systemLogLOG, 'a') as F:
        F.write("=".center(centre, "=") + "\n")
    with open(systemLogLOG, 'a') as F:
        F.write(" \n")


# Effects
def load_wheel(timeNumber):
    loadWheelAnimation = ".", ". .", ". . .", ". . . ."

    for i in range(timeNumber):
        time.sleep(0.1)
        sys.stdout.write("\rLOADING: " + loadWheelAnimation[i % len(loadWheelAnimation)])
        sys.stdout.flush()


def robco_interface(type_function):
    clear()

    empty()

    type_function("ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM".center(centre, " "))
    type_function("COPYRIGHT 2075-2077 ROBCO INDUSTRIES".center(centre, " "))
    with open(server, 'r') as F:
        type_function(F.read().center(centre, " "))
    print(" \n" * 3)


def slide_up():
    for _ in range(30):
        print("")
        time.sleep(0.02)
    clear()


def slide_by_line(filename, delay):
    with open(filename, 'r') as file:
        for line1 in file:
            print(line1, end='')  # Print the line without adding an extra newline
            time.sleep(delay)


def slide_by_line_dir(directory, filename, delay):
    dir_path = os.path.join(directory, filename)
    with open(dir_path, 'r') as file:
        for line1 in file:
            print(line1, end='')  # Print the line without adding an extra newline
            time.sleep(delay)
    empty()


def logo_screen(number):
    print("\n" * number)
    print("██████|  █████| ██████|  █████|  █████| ".center(centre, " "))
    print("██|  ██|██|  ██|██|  ██|██|  ██|██|  ██|".center(centre, " "))
    print("██████| ██|  ██|██████| ██|     ██|  ██|".center(centre, " "))
    print("██|  ██|██|  ██|██|  ██|██|  ██|██|  ██|".center(centre, " "))
    print("██|  ██| █████| ██████|  █████|  █████| ".center(centre, " "))
    print("\n" * number)


def print_slowly(text):
    for line_section in text.split('\n'):
        print(line_section)
        time.sleep(0.05)


# terminal/inquire - - - debug
def t_inquire_code():
    charp("ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL \nENTER PASSWORD NOW")
    with open('system/sevenletterwords.txt') as wordListFile:
        WORDS = wordListFile.readlines()
    for i in range(len(WORDS)):
        WORDS[i] = WORDS[i].strip().upper()

    def main():
        input('\nPress enter to begin protocol...')
        empty()

        gameWords = getWords()
        computerMemory = getComputerMemoryString(gameWords)
        secretPassword = random.choice(gameWords)

        charp(computerMemory)
        for triesRemaining in range(4, 0, -1):
            playerMove = askForPlayerGuess(gameWords, triesRemaining)
            if playerMove == secretPassword:
                charp("\nACCESS GRANTED")
                sys_log2(3, 102, '')
                slide_up()

                main_code()
                return
            else:
                numMatches = numMatchingLetters(secretPassword, playerMove)
                charp('\nAccess Denied ({}/7 correct)'.format(numMatches))
        charp('Out of tries.')
        time.sleep(1)
        clear()
        sys_log2(3, 83, '')

        print("\n" * 14)
        charp("TERMINAL LOCKED".center(centre, " "))
        empty()

        charp("PLEASE CONTACT AN ADMINISTRATOR".center(centre))
        empty()
        time.sleep(10)
        charp("RESTARTING OS_SYSTEM")
        sys_log2(3, 84, '')

    def getWords():
        secretPassword = random.choice(WORDS)
        words = [secretPassword]

        while len(words) < 3:
            randomWord = getOneWordExcept(words)
            if numMatchingLetters(secretPassword, randomWord) == 0:
                words.append(randomWord)

        for b in range(500):
            if len(words) == 5:
                break

            randomWord = getOneWordExcept(words)
            if numMatchingLetters(secretPassword, randomWord) == 3:
                words.append(randomWord)

        for b in range(500):
            if len(words) == 12:
                break

            randomWord = getOneWordExcept(words)
            if numMatchingLetters(secretPassword, randomWord) != 0:
                words.append(randomWord)

        while len(words) < 12:
            randomWord = getOneWordExcept(words)
            words.append(randomWord)

        assert len(words) == 12
        return words

    def getOneWordExcept(blocklist=None):
        if blocklist is None:
            blocklist = []

        while True:
            randomWord = random.choice(WORDS)
            if randomWord not in blocklist:
                return randomWord

    def numMatchingLetters(word1, word2):
        matches = 0
        for a in range(len(word1)):
            if word1[a] == word2[a]:
                matches += 1
            return matches

    def getComputerMemoryString(words):
        linesWithWords = random.sample(range(16 * 2), len(words))
        memoryAddress = 16 * random.randint(0, 4000)

        computerMemory = []
        nextWord = 0
        for lineNum in range(16):
            leftHalf = ''
            rightHalf = ''
            for j in range(16):
                leftHalf += random.choice(GARBAGE_CHARS)
                rightHalf += random.choice(GARBAGE_CHARS)

            if lineNum in linesWithWords:
                insertionIndex = random.randint(0, 9)
                leftHalf = (leftHalf[:insertionIndex] + words[nextWord] + leftHalf[insertionIndex + 7:])
                nextWord += 1

            if lineNum + 16 in linesWithWords:
                insertionIndex = random.randint(0, 9)
                rightHalf = (rightHalf[:insertionIndex] + words[nextWord] + rightHalf[insertionIndex + 7:])
                nextWord += 1

            computerMemory.append('0x' + hex(memoryAddress)[2:].zfill(4)
                                  + '  ' + leftHalf + '    '
                                  + '0x' + hex(memoryAddress + (16 * 16))[2:].zfill(4)
                                  + '  ' + rightHalf)

            memoryAddress += 16

        return '\n'.join(computerMemory)

    def askForPlayerGuess(words, tries):
        while True:
            charp('\nEnter password: ({} tries remaining)'.format(tries))
            guess = input('> ').upper()
            if guess in words:
                return guess
            charp('That is not one of the possible passwords listed above')
            charp('Try entering "{}" or "{}".'.format(words[0], words[1]))

    if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            sys.exit()

    os.system("sudo shutdown -h now")


def t_inquire_sim(simulationText):
    slide_up()

    charp("ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL \nENTER PASSWORD NOW")
    with open(simulationText) as wordListFile:
        WORDS = wordListFile.readlines()
    for i in range(len(WORDS)):
        WORDS[i] = WORDS[i].strip().upper()

    def main():
        input('\nPress enter to begin protocol...')
        empty()

        gameWords = getWords()
        computerMemory = getComputerMemoryString(gameWords)
        secretPassword = random.choice(gameWords)

        charp(computerMemory)
        for triesRemaining in range(4, 0, -1):
            playerMove = askForPlayerGuess(gameWords, triesRemaining)
            if playerMove == secretPassword:
                charp("ACCESS GRANTED")
                slide_up()

                return
            else:
                numMatches = numMatchingLetters(secretPassword, playerMove)
                charp('Access Denied ({}/7 correct)'.format(numMatches))
        charp('Out of tries. Secret password was {}.'.format(secretPassword))
        time.sleep(1)

    def getWords():
        secretPassword = random.choice(WORDS)
        words = [secretPassword]

        while len(words) < 3:
            randomWord = getOneWordExcept(words)
            if numMatchingLetters(secretPassword, randomWord) == 0:
                words.append(randomWord)

        for b in range(500):
            if len(words) == 5:
                break

            randomWord = getOneWordExcept(words)
            if numMatchingLetters(secretPassword, randomWord) == 3:
                words.append(randomWord)

        for b in range(500):
            if len(words) == 12:
                break

            randomWord = getOneWordExcept(words)
            if numMatchingLetters(secretPassword, randomWord) != 0:
                words.append(randomWord)

        while len(words) < 12:
            randomWord = getOneWordExcept(words)
            words.append(randomWord)

        assert len(words) == 12
        return words

    def getOneWordExcept(blocklist=None):
        if blocklist is None:
            blocklist = []

        while True:
            randomWord = random.choice(WORDS)
            if randomWord not in blocklist:
                return randomWord

    def numMatchingLetters(word1, word2):
        matches = 0
        for a in range(len(word1)):
            if word1[a] == word2[a]:
                matches += 1
            return matches

    def getComputerMemoryString(words):
        linesWithWords = random.sample(range(16 * 2), len(words))
        memoryAddress = 16 * random.randint(0, 4000)

        computerMemory = []
        nextWord = 0
        for lineNum in range(16):
            leftHalf = ''
            rightHalf = ''
            for j in range(16):
                leftHalf += random.choice(GARBAGE_CHARS)
                rightHalf += random.choice(GARBAGE_CHARS)

            if lineNum in linesWithWords:
                insertionIndex = random.randint(0, 9)
                leftHalf = (leftHalf[:insertionIndex] + words[nextWord] + leftHalf[insertionIndex + 7:])
                nextWord += 1

            if lineNum + 16 in linesWithWords:
                insertionIndex = random.randint(0, 9)
                rightHalf = (rightHalf[:insertionIndex] + words[nextWord] + rightHalf[insertionIndex + 7:])
                nextWord += 1

            computerMemory.append('0x' + hex(memoryAddress)[2:].zfill(4)
                                  + '  ' + leftHalf + '    '
                                  + '0x' + hex(memoryAddress + (16 * 16))[2:].zfill(4)
                                  + '  ' + rightHalf)

            memoryAddress += 16

        return '\n'.join(computerMemory)

    def askForPlayerGuess(words, tries):
        while True:
            charp('\nEnter password: ({} tries remaining)'.format(tries))
            guess = input('> ').upper()
            if guess in words:
                return guess
            charp('That is not one of the possible passwords listed above')
            charp('Try entering "{}" or "{}".'.format(words[0], words[1]))

    if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            sys.exit()


# Add, View, CLear
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
    empty()


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
            charp(file.read())
            empty()

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


# Msis code
def msis_main():
    robco_interface(print)

    header_charp("MILITARY SILO INVENTORY SYSTEM", "-")
    charp("| " + currentDate + " | ID: " + encrypt_user(random.randint(20, 70)))
    empty()

    time.sleep(2)
    robco_interface(print)
    line()

    slide_by_line(msis, delay=0.025)
    line()

    empty()

    back(3, 6)


# Entry logs
def entry_logs_main():
    robco_interface(print)

    header_charp("ENTRY LOGS", "-")
    while True:
        robco_interface(print)

        header_print("ENTRY LOGS", "-")
        entryChoice = ["Add new terminal entry", "View terminal entry", "Clear terminal entry", "Return"]
        entry_choice_menu = TerminalMenu(entryChoice)
        entry_index = entry_choice_menu.show()
        entrySelection = entryChoice[entry_index]
        if entrySelection == "Add new terminal entry":
            sys_log2(3, 55, "terminal-entry")
            robco_interface(print)

            add_entry(journal_dir)

            back(3, 6)
        if entrySelection == "View terminal entry":
            sys_log2(3, 53, "terminal-entry")
            robco_interface(print)

            view_entry(journal_dir)

            back(3, 6)
        if entrySelection == "Clear terminal entry":
            sys_log2(3, 19, "terminal-entry")
            robco_interface(print)

            clear_entry(journal_dir)

            back(3, 6)
        if entrySelection == "Return":
            return_menu(3, 6)

            break


# Network
def network_main():
    robco_interface(print)

    header_charp("NETWORK", "-")

    charp("| Computer system: " + hostname)
    charp("\n| Computer system IP Address: " + ipaddr)
    empty()

    print(os.system('ipconfig getifaddr en0'), "\n")
    print(os.system('curl ifconfig.me'))
    empty()

    back(3, 6)


# cmd-Terminal
def cmd_main():
    robco_interface(print)

    header_charp("CMD TERMINAL", "-")

    while True:
        charp("| [ctrl + C] to break command ")
        charp("| [BACK] ")
        input_char("| > ")
        tDirectoryInput = input("")
        for char in ((os.system(tDirectoryInput)),):
            print(char, end='')
            sys.stdout.flush()
            time.sleep(0.01)
        sys_log2(3, 51, tDirectoryInput)

        if tDirectoryInput == "BACK":
            slide_up()

            return_menu(3, 6)

            break


# Contacts
def contacts_main():
    robco_interface(print)

    header_charp("CONTACTS", "-")
    charp(progressI)
    back(3, 6)


# Inquire sim
def t_inquire_sim_main():
    while True:
        robco_interface(print)

        header_charp("HACKING/INQUIRE SIMULATOR", "-")

        hackSimOptions = ["7 Letter word hack", "BACK"]
        hackSim_menu = TerminalMenu(hackSimOptions)
        hackSim_entry_index = hackSim_menu.show()
        hackSimSelection = hackSimOptions[hackSim_entry_index]
        if hackSimSelection == "7 Letter word hack":
            t_inquire_sim("system/sevenletterwords.txt")
        if hackSimSelection == "BACK":
            return_menu(3, 6)

            break


# Data Archive
def data_archive_main():
    robco_interface(print)

    header_charp("DATA ARCHIVE", "-")
    while True:
        robco_interface(print)

        header_print("DATA ARCHIVE", "-")
        entryChoice = ["Add new archive entry", "View archive entry", "Clear archive entry", "Return"]
        entry_choice_menu = TerminalMenu(entryChoice)
        entry_index = entry_choice_menu.show()
        entrySelection = entryChoice[entry_index]
        if entrySelection == "Add new archive entry":
            sys_log2(3, 55, "archive-entry")
            robco_interface(print)

            add_entry(archive_dir)

            back(3, 6)
        if entrySelection == "View archive entry":
            sys_log2(3, 53, "archive-entry")
            robco_interface(print)

            view_entry(archive_dir)

            back(3, 6)
        if entrySelection == "Clear archive entry":
            sys_log2(3, 19, "archive-entry")
            robco_interface(print)

            clear_entry(archive_dir)

            back(3, 6)
        if entrySelection == "Return":
            return_menu(3, 6)

            break


# System Diagnostics
def system_diagnostics_main():
    robco_interface(print)

    header_charp("SYSTEM DIAGNOSTICS", "-")

    while True:
        robco_interface(print)

        header_print("SYSTEM DIAGNOSTICS", "-")

        main_system_diagnostics_report()
        sys_log2(3, 33, "system_diagnostics < run")

        systemChoice = ["View System Performance Report", "Backup Data", "Reboot System", "Return"]
        system_choice_menu = TerminalMenu(systemChoice)
        system_entry_index = system_choice_menu.show()
        systemSelection = systemChoice[system_entry_index]
        if systemSelection == "View System Performance Report":
            sys_log2(3, 53, "system_performance_report")
            robco_interface(print)

            view_system_performance_report()

            back(3, 6)
        if systemSelection == "Backup Data":
            sys_log2(3, 23, "data < w/s")
            robco_interface(print)

            backup_data(directoryB_paths, backup_location)

            back(3, 6)
        if systemSelection == "Reboot System":
            sys_log2(3, 104, "@exit reboot")
            sys_log2(3, 104, "- reboot imminent @exit < s")
            robco_interface(print)

            reboot_system()

            back(3, 6)
        if systemSelection == "Return":
            return_menu(3, 6)

            break


# System Log
def system_log_main():
    robco_interface(print)

    header_charp("SYSTEM LOG", "-")
    slide_by_line('system/system-logs.log', delay=0.01)
    empty()

    back(3, 6)


# Password
def store_password(file_path, hashed_password):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as F:
        F.write(hashed_password)


def read_password(file_path):
    with open(file_path, 'rb') as F:
        return F.read()


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password)


def encrypt_password(plain_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode(), salt)
    return hashed_password


# - - - - - Main Setting's Code(s)
# Settings
def settings_menu():
    def clearance_m():
        while True:
            sys_log2(3, 47, "clearance_m")
            robco_interface(print)
            header_print("SETTINGS", "-")

            clearanceOptions = ["View clearance", "Return"]
            clearance_menu = TerminalMenu(clearanceOptions)
            clearance_entry_index = clearance_menu.show()
            clearanceSelection = clearanceOptions[clearance_entry_index]
            if clearanceSelection == "View clearance":
                with open(clearanceTXT, 'r') as F:
                    charp(F.read())
                    back(3, 6)
            if clearanceSelection == "Return":
                return_menu(3, 6)

                break

    def credentials_m():
        while True:
            sys_log2(3, 47, "cred_m")
            robco_interface(print)
            header_print("SETTINGS", "-")

            credentialOptions = ["View credentials", "Change credentials", "Return"]
            credential_menu = TerminalMenu(credentialOptions)
            credential_entry_index = credential_menu.show()
            credentialsSelection = credentialOptions[credential_entry_index]
            if credentialsSelection == "View credentials":
                with open(credTXT, 'r') as F:
                    charp(F.read())
                    back(3, 6)
            if credentialsSelection == "Change credentials":
                with open(credTXT, 'w') as F:
                    F.write("")
                    passwordEntry = input("> ")
                with open(credTXT, 'a') as F:
                    F.write(passwordEntry)
                charp("Credentials changed to " + credential)
                back(3, 6)
            if credentialsSelection == "Return":
                return_menu(3, 6)

                break

    def password_m():
        charp("ENTER PASSWORD NOW > ")
        passwordPASSWORD = encoded_input("")
        try:
            stored_hashed_password = read_password('user_info/password.txt')
        except FileNotFoundError:
            print("Password file not found. Please set up your password first.")
            return

        if verify_password(passwordPASSWORD, stored_hashed_password):

            while True:
                sys_log2(3, 47, "password_m")
                robco_interface(print)

                header_print("SETTINGS", "-")

                passwordOptions = ["View password", "Change password", "Return"]
                password_menu = TerminalMenu(passwordOptions)
                password_entry_index = password_menu.show()
                passwordSelection = passwordOptions[password_entry_index]
                if passwordSelection == "View password":
                    charp(f"Current password: {read_password(PasswordTXT)}")
                    back(3, 6)
                if passwordSelection == "Change password":
                    passEntry = getpass("Enter your new password: ")
                    hashed_password = encrypt_password(passEntry)
                    store_password('user_info/password.txt', hashed_password)
                    print("Password stored successfully.")
                    empty()

                    charp(f"Password changed to: {passEntry}")
                    back(3, 6)
                if passwordSelection == "Return":
                    return_menu(3, 6)

                    break

    def username_m():
        while True:
            sys_log2(3, 47, "username_m")
            robco_interface(print)
            header_print("SETTINGS", "-")

            usernameOptions = ["View username", "Change Username", "Return"]
            username_menu = TerminalMenu(usernameOptions)
            username_entry_index = username_menu.show()
            usernameSelection = usernameOptions[username_entry_index]
            if usernameSelection == "View username":
                with open(UserTXT, 'r') as F:
                    charp(F.read())
                    back(3, 6)
            if usernameSelection == "Change Username":
                with open(UserTXT, 'w') as F:
                    F.write("")
                usernameEntry = input("> ")
                with open(UserTXT, 'a') as F:
                    F.write(usernameEntry)
                charp("Username changed to " + usernameEntry)
                back(3, 6)
            if usernameSelection == "Return":
                return_menu(3, 6)

                break

    while True:
        robco_interface(print)

        header_charp("SETTINGS", "-")

        charp("RobCoOS " + softwareV)
        charp("ⓒ" + year + " RobCo")
        empty()

        charp("SalliOS " + salliV)
        charp(ai)
        empty()
        empty()

        settingsOption = ["Username", "Password", "Credentials", "Clearance", "Return"]
        settingsCLI_menu = TerminalMenu(settingsOption)
        settings_entry_index = settingsCLI_menu.show()
        settingsSelection = settingsOption[settings_entry_index]
        if settingsSelection == "Username":
            username_m()
        if settingsSelection == "Password":
            password_m()
        if settingsSelection == "Credentials":
            credentials_m()
        if settingsSelection == "Clearance":
            clearance_m()
        if settingsSelection == "Return":
            return_menu(3, 6)

            break


# Restart
def restart_menu():
    clear()

    empty()

    sys_log2(3, 10, "logon.F")
    exit_info("RESTARTING SYSTEM")
    locate_file_screen()

    slide_up()


# Exit
def exit_menu():
    clear()

    empty()

    sys_log2(3, 14, "")
    exit_info("POWERING OFF TERMINAL")
    exit()


# Shutdown
def shutdown_menu():
    header_charp("SHUTDOWN MENU", " ")

    shutDownOptions = ["Confirm", "Abort"]
    shutDownC_menu = TerminalMenu(shutDownOptions)
    shutDown_entry_index = shutDownC_menu.show()
    shutDownChoice = shutDownOptions[shutDown_entry_index]
    if shutDownChoice == "Confirm":
        sys_log2(3, 72, "")
        slide_up()

        clear()

        exit_info("SHUTTING DOWN")

        # Shuts down Operating System / Computer for Linux/Apple
        os.system("sudo shutdown -h now")
    if shutDownChoice == "Abort":
        sys_log2(3, 73, "")
        charp("| Shutdown aborted")
        return_menu(3, 7)


# Emergency Protocols
def emergency_protocols_main():
    robco_interface(print)

    header_charp("EMERGENCY PROTOCOLS", "-")

    while True:
        header_print("EMERGENCY PROTOCOLS", "-")
        emergencyChoice = ["New Emergency Protocols", "View Emergency Protocols", "Clear Emergency Protocols", "Return"]
        emergency_choice_menu = TerminalMenu(emergencyChoice)
        emergency_entry_index = emergency_choice_menu.show()
        emergencySelection = emergencyChoice[emergency_entry_index]
        if emergencySelection == "New Emergency Protocol":
            sys_log2(3, 55, "emergency-protocol")

            robco_interface(print)

            add_entry(emergencyProtocol_dir)

            back(3, 6)
        if emergencySelection == "View Emergency Protocols":
            sys_log2(3, 53, "emergency-protocol")

            robco_interface(print)

            view_entry(emergencyProtocol_dir)

            back(3, 6)
        if emergencySelection == "Clear Emergency Protocol":
            sys_log2(3, 19, "emergency-protocol")

            robco_interface(print)

            clear_entry(emergencyProtocol_dir)

            back(3, 6)
        if emergencySelection == "Return":
            return_menu(3, 6)

            break


# Security
def security_main():
    def security_protocols():
        robco_interface(print)

        header_charp("SECURITY PROTOCOLS", "-")

        while True:
            robco_interface(print)
            header_print("SECURITY PROTOCOLS", "-")

            archiveChoice = ["New Security Protocol", "View Security Protocols", "Clear Security Protocol", "Return"]
            archive_choice_menu = TerminalMenu(archiveChoice)
            archive_entry_index = archive_choice_menu.show()
            archiveSelection = archiveChoice[archive_entry_index]
            if archiveSelection == "New Security Protocol":
                robco_interface(print)

                add_entry(protocols_dir)

                back(3, 6)
            if archiveSelection == "View Security Protocols":
                robco_interface(print)

                view_entry(protocols_dir)

                back(3, 6)
            if archiveSelection == "Clear Security Protocol":
                robco_interface(print)

                clear_entry(protocols_dir)

                back(3, 6)
            if archiveSelection == "Return":
                return_menu(3, 6)

                break

    def security_level():
        robco_interface(print)

        header_charp("SECURITY LEVEL", "-")

        while True:
            robco_interface(print)
            header_print("SECURITY LEVEL", "-")

            charp("Current Security Level : " + securityLevel)
            charp("Security Level Reason  : " + securityLvlRR)
            charp("Available Levels: ")
            empty()

            archiveChoice = ["Low", "Medium", "High", "BACK"]
            archive_choice_menu = TerminalMenu(archiveChoice)
            archive_entry_index = archive_choice_menu.show()
            archiveSelection = archiveChoice[archive_entry_index]
            if archiveSelection == "Low":
                robco_interface(print)

                with open(securitylvlTXT, 'w') as F:
                    F.write("")
                with open(securitylvlTXT, 'a') as F:
                    F.write("LOW")
                input_char("Security level reasoning: ")
                SlvlR = input("")
                with open(securityrlvlTXT, 'w') as F:
                    F.write("")
                with open(securityrlvlTXT, 'a') as F:
                    F.write(SlvlR)

                charp("SECURITY LEVEL UPDATED TO: LOW")

                back(3, 6)
            if archiveSelection == "Medium":
                robco_interface(print)

                with open(securitylvlTXT, 'w') as F:
                    F.write("")
                with open(securitylvlTXT, 'a') as F:
                    F.write("HIGH")
                input_char("Security level reasoning: ")
                SlvlR = input("")
                with open(securityrlvlTXT, 'w') as F:
                    F.write("")
                with open(securityrlvlTXT, 'a') as F:
                    F.write(SlvlR)

                charp("SECURITY LEVEL UPDATED TO: MEDIUM")

                back(3, 6)
            if archiveSelection == "High":
                robco_interface(print)

                with open(securitylvlTXT, 'w') as F:
                    F.write("")
                with open(securitylvlTXT, 'a') as F:
                    F.write("HIGH")
                input_char("Security level reasoning: ")
                SlvlR = input("")
                with open(securityrlvlTXT, 'w') as F:
                    F.write("")
                with open(securityrlvlTXT, 'a') as F:
                    F.write(SlvlR)

                charp("SECURITY LEVEL UPDATED TO: HIGH")

                back(3, 6)
            if archiveSelection == "BACK":
                return_menu(3, 6)

                break

    def security_logs_main():
        robco_interface(print)

        header_charp("SECURITY LOGS", "-")

        while True:
            robco_interface(print)
            header_print("SECURITY LOGS", "-")

            archiveChoice = ["New Security Entry", "View Security Entry", "Clear Security Entry", "BACK"]
            archive_choice_menu = TerminalMenu(archiveChoice)
            archive_entry_index = archive_choice_menu.show()
            archiveSelection = archiveChoice[archive_entry_index]
            if archiveSelection == "New Security Entry":
                robco_interface(print)

                add_entry(security_dir)

                back(3, 6)
            if archiveSelection == "View Security Entry":
                robco_interface(print)

                view_entry(security_dir)

                back(3, 6)
            if archiveSelection == "Clear Security Entry":
                robco_interface(print)

                clear_entry(security_dir)

                back(3, 6)
            if archiveSelection == "BACK":
                return_menu(3, 6)

                break

    robco_interface(print)

    header_charp("SECURITY SETTINGS", "-")

    while True:
        robco_interface(print)
        header_print("SECURITY SETTINGS", "-")

        protocolChoice = ["Security Logs", "Adjust Security Level", "Update Security Protocols", "Return"]
        protocol_choice_menu = TerminalMenu(protocolChoice)
        protocol_entry_index = protocol_choice_menu.show()
        protocolSelection = protocolChoice[protocol_entry_index]
        if protocolSelection == "Security Logs":
            sys_log2(3, 12, "security-logs")

            robco_interface(print)

            security_logs_main()
        if protocolSelection == "Adjust Security Level":
            sys_log2(3, 61, "security-level")

            robco_interface(print)

            security_level()
        if protocolSelection == "Update Security Protocols":
            sys_log2(3, 106, "security-protocols")

            robco_interface(print)

            security_protocols()
        if protocolSelection == "Return":
            return_menu(3, 6)

            break


# Maintenance
def maintenance_main():
    robco_interface(print)

    header_charp("MAINTENANCE REQUESTS/LOG", "-")
    charp(progressI)
    back(3, 6)


# - - - - - Main code
def main_code():
    slide_up()

    robco_interface(charp)

    while True:
        lineSection = 2
        sys_log2(lineSection, 67, "main_menuDIR")
        robco_interface(print)

        charp("Security level: " + securityLevel)
        empty()

        menu = ["Country Missile Silo Inventory System", "Entry Logs", "Network",
                "RobCo cmd-Terminal", "Contacts", "Hacking/inquire Simulator", "Data Archive", "System Diagnostics",
                "System Log", "--".center(centre, "-"),
                "[SETTINGS]    - RobCo Terminal Settings and User Management",
                "[EMERGENCY]   - Emergency Protocols",
                "[MAINTENANCE] - Maintenance Requests and Logs",
                "[SECURITY]    - Security Settings",
                "[RESTART]     - Restart Terminal",
                "[EXIT]        - Exit Terminal ProgramOS",
                "[SHUTDOWN]    - Shutdown Entire OS",
                "[LOGOUT]      - Logout of Terminal"]
        terminal_menu = TerminalMenu(menu)
        menu_entry_index = terminal_menu.show()
        selection = menu[menu_entry_index]
        if selection == "Country Missile Silo Inventory System":
            sys_log2(lineSection, 12, 'msis_m')
            msis_main()
        if selection == "Entry Logs":
            sys_log2(lineSection, 12, 'entry-logs_m')
            entry_logs_main()
        if selection == "Network":
            sys_log2(lineSection, 12, 'network_m')
            network_main()
        if selection == "RobCo cmd-Terminal":
            sys_log2(lineSection, 12, 'cmd-Term_m')
            cmd_main()
        if selection == "Contacts":
            sys_log2(lineSection, 12, 'contacts_m')
            contacts_main()
        if selection == "Hacking/inquire Simulator":
            sys_log2(lineSection, 12, 'inquire-sim_m')
            t_inquire_sim_main()
        if selection == "Data Archive":
            sys_log2(lineSection, 12, 'data-archive_m')
            data_archive_main()
        if selection == "System Diagnostics":
            sys_log2(lineSection, 12, 'diagnostics_m')
            system_diagnostics_main()
        if selection == "System Log":
            sys_log2(lineSection, 12, 'sys-logs_m')
            system_log_main()
        if selection == "[SETTINGS]    - RobCo Terminal Settings and User Management":
            sys_log2(lineSection, 12, 'settings_m')
            settings_menu()
        if selection == "[EMERGENCY]   - Emergency Protocols":
            sys_log2(lineSection, 12, 'emergency_m')
            emergency_protocols_main()
        if selection == "[MAINTENANCE] - Maintenance Requests and Logs":
            sys_log2(lineSection, 12, 'maintenance_m')
            maintenance_main()
        if selection == "[SECURITY]    - Security Settings":
            sys_log2(lineSection, 12, 'security_m')
            security_main()
        if selection == "[RESTART]     - Restart Terminal":
            sys_log2(lineSection, 12, 'restart_m')
            restart_menu()
        if selection == "[SHUTDOWN]    - Shutdown Entire OS":
            sys_log2(lineSection, 12, "shutdown_m")
            clear()
            shutdown_menu()
        if selection == "[EXIT]        - Exit Terminal ProgramOS":
            sys_log2(lineSection, 12, "exit_m")
            exit_menu()
        if selection == "[LOGOUT]      - Logout of Terminal":
            sys_log2(lineSection, 12, 'logout_m')
            sys_log2(lineSection + 1, 17, currentUser)
            clear()

            exit_info("LOGGING OUT OF TERMINAL")

            header_charp("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK", " ")
            charp("capslock-input set: off")
            sys_log(2, '')
            empty()

            break


#
#
#
#
# ---------- Main code ----------

sys_logEmpty()
sys_log(1, '')

locate_file_screen()

slide_up()

# terminal opening mainframe
header_charp("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK", " ")
charp("capslock-input set: off")
sys_log(2, '')
empty()

while True:
    empty()

    input_char("> ")
    terminalInput = input("")
    if terminalInput == "logon " + user:
        currentUser = user
        sys_log2(1, 16, currentUser)
        empty()
        try:
            stored_hashed_password = read_password('user_info/password.txt')
        except FileNotFoundError:
            charp("Password file not found. Please set up your password first.")
            break

        charp("Enter password now")
        empty()
        empty()

        input_char("> ")

        passwordInput = encoded_input("")
        if verify_password(passwordInput, stored_hashed_password):
            sys_log2(1, 74, '')
            sys_log2(2, 100, currentUser)

            main_code()

        else:
            sys_log2(1, 75, '')
            empty()

            charp("| Incorrect password entered")
            empty()
    if terminalInput == "set terminal/inquire":
        sys_log2(1, 79, "")
        empty()

        charp("RIT-V300\n")
        empty()

        charp("> ")
        InputCOMMANDline = input("")
        if InputCOMMANDline == "set file/protection=owner:rwed accounts.f":
            sys_log2(1, 80, "")
            charp("> ")
            InputCOMMANDline2 = input("")
            if InputCOMMANDline2 == "set halt restart/maint":
                sys_log2(2, 81, "")
                empty()

                charp("Initialising Robco Industries(TM) MF Boot Agent v2.3.0 \nRETROS BIOS \nRBIOS-4.02.08.00 "
                      "52EE5.E7.E8 \nCopyright 2201-2203 Robco Ind. \nUppermem: 64 KB \nRoot (5A8) \nMaintenance Mode\n")
                empty()

                charp("> ")
                InputCOMMANDline3 = input("")
                if InputCOMMANDline3 == "run debug/accounts.f":
                    sys_log2(2, 81, "")
                    slide_up()

                    t_inquire_code()
    if terminalInput == "shutdown":
        sys_log2(1, 12, "shutdown_m")
        shutdown_menu()

        header_charp("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK", " ")
        charp("capslock-input set: off")
    if terminalInput == "help":
        sys_log2(1, 12, "help_m")
        empty()

        line()

        slide_by_line("system/help-menu.txt", delay=0.03)
    if terminalInput == "exit":
        sys_log2(1, 59, "terminal.py")
        exit_menu()
    if terminalInput == "set terminal/system-logs":
        sys_log2(1, 12, "system-logs")
        input_char("> ")
        setTerminal_command = input("")
        if setTerminal_command == "set file/overwrite=clear":
            sys_log2(1, 21, "system-logs")
            charp("system_logs has been reset")
            with open(systemLogLOG, 'w') as f:
                f.write("")
            sys_logEmpty()
            sys_log(1, "> after @reset-log * * *")
    if terminalInput == "error_dir":
        sys_log2(1, 12, "error_dir")
        charp("ALL ERROR CODES RobCo_OS Terminal:")
        empty()

        slide_by_line_dir(error_dir, "0x0AABFF00.txt", delay=0.02)
        slide_by_line_dir(error_dir, "0x0D890102.txt", delay=0.02)
        slide_by_line_dir(error_dir, "0x00B636C6.txt", delay=0.02)
        slide_by_line_dir(error_dir, "0x03C663A1.txt", delay=0.02)
        slide_by_line_dir(error_dir, "0x07F6BAAC.txt", delay=0.02)
        slide_by_line_dir(error_dir, "0x357C5001.txt", delay=0.02)
        slide_by_line_dir(error_dir, "0x00001001.txt", delay=0.02)
        slide_by_line_dir(error_dir, "0x00001011.txt", delay=0.02)
        slide_by_line_dir(error_dir, "0xA001C007.txt", delay=0.02)
        slide_by_line_dir(error_dir, "0xF141A013.txt", delay=0.02)
        slide_by_line_dir(error_dir, "0xFA770171.txt", delay=0.02)
        slide_by_line_dir(error_dir, "0xFFF11011.txt", delay=0.02)
        slide_by_line("system/corrupt-error.txt", delay=0.02)
    if terminalInput == "clear":
        sys_log2(1, 19, "@screen")
        slide_up()

        header_charp("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK", " ")
        charp("capslock-input set: off")
        empty()
    handle_command(terminalInput)
