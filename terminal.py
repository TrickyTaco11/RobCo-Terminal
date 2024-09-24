#
#
#
#
# Based from Fallout 3 and 4's terminal system while taking inspiration from old CRT terminals from the 60's.
# This project is designed to run in terminal or a terminal emulator, preferably in 'cool-retro-term'.
#
#
#
#
#
# ---------- Imports ----------

import logging

import var_RobCo
import sys_RobCo
import cmd_RobCo
import termS_RobCo
import e_RobCo
import mainCode_RobCo
import maint_RobCo


# ---------- Main Code ----------

logging.basicConfig(
    filename='system/system-logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

sys_RobCo.e_log()
sys_RobCo.m_log(1, '')

termS_RobCo.locate_file_screen()
termS_RobCo.slide_up()

# terminal basic
termS_RobCo.header_("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK", " ", cmd_RobCo.char)
cmd_RobCo.char("capslock-input set: off")
sys_RobCo.m_log(2, '')

while True:
    termS_RobCo.empty()

    cmd_RobCo.input_char("> ")
    terminalInput = input("")
    if terminalInput == 'logon ' + var_RobCo.user:
        sys_RobCo.log(1, 16, var_RobCo.user)
        termS_RobCo.empty()

        try:
            stored_hashed_password = e_RobCo.read_password('user_info/password.txt')
        except FileNotFoundError:
            cmd_RobCo.char("Password file not found. Please reset/clear your password.txt")
            break

        cmd_RobCo.char("Enter password now")
        termS_RobCo.empty()
        cmd_RobCo.input_char("> ")

        passwordInput = e_RobCo.encoded_input("")
        if e_RobCo.verify_password(passwordInput, stored_hashed_password):
            sys_RobCo.log(1, 74, '')
            sys_RobCo.log(2, 100, var_RobCo.user)

            mainCode_RobCo.main_code()

        else:
            cmd_RobCo.char("Incorrect password entered")
    elif terminalInput == "set terminal/inquire":
        sys_RobCo.log(1, 79, "")
        termS_RobCo.empty()

        cmd_RobCo.char("RIT-V300")
        termS_RobCo.empty()

        cmd_RobCo.input_char("> ")
        InputCOMMANDline = input("")
        if InputCOMMANDline == "set file/protection=owner:rwed accounts.f":
            sys_RobCo.log(1, 80, "")
            cmd_RobCo.input_char("> ")
            InputCOMMANDline2 = input("")
            if InputCOMMANDline2 == "set halt restart/maint":
                sys_RobCo.log(2, 81, "")
                termS_RobCo.empty()
                with open(var_RobCo.maintenanceLogTXT, 'a') as file:
                    file.write(f"{var_RobCo.currentTime}: Maintenance Log: \n"
                               "Initialising Robco Industries(TM) MF Boot Agent v2.3.0 \nRETROS BIOS "
                               "\nRBIOS-4.02.08.00 "
                               "52EE5.E7.E8 \nCopyright 2201-2203 Robco Ind. \nUppermem: 64 KB \nRoot (5A8) "
                               "\nMaintenance Mode\n. \n. "
                               )

                cmd_RobCo.char("Initialising Robco Industries(TM) MF Boot Agent v2.3.0 \nRETROS BIOS "
                               "\nRBIOS-4.02.08.00 "
                               "52EE5.E7.E8 \nCopyright 2201-2203 Robco Ind. \nUppermem: 64 KB \nRoot (5A8) "
                               "\nMaintenance "
                               "Mode")
                termS_RobCo.empty()

                cmd_RobCo.input_char("> ")
                InputCOMMANDline3 = input("")
                if InputCOMMANDline3 == "run debug/accounts.f":
                    sys_RobCo.log(2, 81, "")
                    termS_RobCo.slide_up()

                    maint_RobCo.t_inquire_code()

        termS_RobCo.empty()
        cmd_RobCo.char("? syntax error")
    elif terminalInput == "help":
        sys_RobCo.log(1, 12, "help_m")
        termS_RobCo.empty()
        termS_RobCo.slide_by_line("system/help-menu.txt", delay=0.03)
    elif terminalInput == "clear":
        sys_RobCo.log(1, 19, "@screen")
        termS_RobCo.slide_up()
        termS_RobCo.header_("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK", " ", print)
        print("capslock-input set: off")
        termS_RobCo.empty()

    elif cmd_RobCo.handle_command(terminalInput):
        continue

    else:
        termS_RobCo.empty()
        cmd_RobCo.char("? syntax error")
