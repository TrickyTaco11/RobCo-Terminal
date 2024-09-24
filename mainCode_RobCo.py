from simple_term_menu import TerminalMenu
from getpass import getpass

import random
import time
import sys
import os

import termS_RobCo
import maint_RobCo
import func_RobCo
import cmd_RobCo
import sys_RobCo
import var_RobCo
import e_RobCo


# main code
def main_code():
    termS_RobCo.slide_up()

    termS_RobCo.robco_interface(cmd_RobCo.char)

    while True:
        lineSection = 2
        sys_RobCo.log(lineSection, 67, "main_menuDIR")
        termS_RobCo.robco_interface(print)

        cmd_RobCo.char("Security level: " + var_RobCo.securityLevel)
        termS_RobCo.empty()

        menu = ["Country Missile Silo Inventory System", "Entry Logs", "Network",
                "RobCo cmd-Terminal", "Contacts", "Hacking/inquire Simulator", "Data Archive", "System Diagnostics",
                "System Log", "--".center(var_RobCo.centre, "-"),
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
            sys_RobCo.log(lineSection, 12, 'msis_m')
            msis_main()
        if selection == "Entry Logs":
            sys_RobCo.log(lineSection, 12, 'entry-logs_m')
            entry_logs_main()
        if selection == "Network":
            sys_RobCo.log(lineSection, 12, 'network_m')
            network_main()
        if selection == "RobCo cmd-Terminal":
            sys_RobCo.log(lineSection, 12, 'cmd-Term_m')
            cmd_main()
        if selection == "Contacts":
            sys_RobCo.log(lineSection, 12, 'contacts_m')
            contacts_main()
        if selection == "Hacking/inquire Simulator":
            sys_RobCo.log(lineSection, 12, 'inquire-sim_m')
            t_inquire_sim_main()
        if selection == "Data Archive":
            sys_RobCo.log(lineSection, 12, 'data-archive_m')
            data_archive_main()
        if selection == "System Diagnostics":
            sys_RobCo.log(lineSection, 12, 'diagnostics_m')
            system_diagnostics_main()
        if selection == "System Log":
            sys_RobCo.log(lineSection, 12, 'sys-logs_m')
            system_log_main()
        if selection == "[SETTINGS]    - RobCo Terminal Settings and User Management":
            sys_RobCo.log(lineSection, 12, 'settings_m')
            settings_menu()
        if selection == "[EMERGENCY]   - Emergency Protocols":
            sys_RobCo.log(lineSection, 12, 'emergency_m')
            emergency_protocols_main()
        if selection == "[MAINTENANCE] - Maintenance Requests and Logs":
            sys_RobCo.log(lineSection, 12, 'maintenance_m')
            maintenance_main()
        if selection == "[SECURITY]    - Security Settings":
            sys_RobCo.log(lineSection, 12, 'security_m')
            security_main()
        if selection == "[RESTART]     - Restart Terminal":
            sys_RobCo.log(lineSection, 12, 'restart_m')
            restart_menu()
        if selection == "[SHUTDOWN]    - Shutdown Entire OS":
            sys_RobCo.log(lineSection, 12, "shutdown_m")
            cmd_RobCo.clear()
            shutdown_menu()
        if selection == "[EXIT]        - Exit Terminal ProgramOS":
            sys_RobCo.log(lineSection, 12, "exit_m")
            exit_menu()
        if selection == "[LOGOUT]      - Logout of Terminal":
            sys_RobCo.log(lineSection, 12, 'logout_m')
            sys_RobCo.log(lineSection + 1, 17, var_RobCo.user)
            cmd_RobCo.clear()

            func_RobCo.exit_info("LOGGING OUT OF TERMINAL")

            termS_RobCo.header_("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK", " ", cmd_RobCo.char)
            cmd_RobCo.char("capslock-input set: off")
            sys_RobCo.m_log(2, '')
            termS_RobCo.empty()

            break


# 1
# msis code
def msis_main():
    termS_RobCo.robco_interface(print)

    termS_RobCo.header_("MILITARY SILO INVENTORY SYSTEM", "-", cmd_RobCo.char)
    cmd_RobCo.char("| " + var_RobCo.currentDate + " | ID: " + e_RobCo.encrypt_user(random.randint(20, 70)))
    termS_RobCo.empty()

    time.sleep(2)
    termS_RobCo.robco_interface(print)
    termS_RobCo.line()

    termS_RobCo.slide_by_line(var_RobCo.msis, delay=0.025)
    termS_RobCo.line()

    termS_RobCo.line()

    func_RobCo.back(3, 6)


# entry logs code
def entry_logs_main():
    termS_RobCo.robco_interface(print)

    termS_RobCo.header_("ENTRY LOGS", "-", print)
    while True:
        termS_RobCo.robco_interface(print)

        termS_RobCo.header_("ENTRY LOGS", "-", print)
        entryChoice = ["Add new terminal entry", "View terminal entry", "Clear terminal entry", "Return"]
        entry_choice_menu = TerminalMenu(entryChoice)
        entry_index = entry_choice_menu.show()
        entrySelection = entryChoice[entry_index]
        if entrySelection == "Add new terminal entry":
            sys_RobCo.log(3, 55, "terminal-entry")
            termS_RobCo.robco_interface(print)

            func_RobCo.add_entry(var_RobCo.journal_dir)

            func_RobCo.back(3, 6)
        if entrySelection == "View terminal entry":
            sys_RobCo.log(3, 53, "terminal-entry")
            termS_RobCo.robco_interface(print)

            func_RobCo.view_entry(var_RobCo.journal_dir)

            func_RobCo.back(3, 6)
        if entrySelection == "Clear terminal entry":
            sys_RobCo.log(3, 19, "terminal-entry")
            termS_RobCo.robco_interface(print)

            func_RobCo.clear_entry(var_RobCo.journal_dir)

            func_RobCo.back(3, 6)
        if entrySelection == "Return":
            func_RobCo.return_menu(3, 6)

            break


# network code
def network_main():
    termS_RobCo.robco_interface(print)

    termS_RobCo.header_("NETWORK", "-", cmd_RobCo.char)

    cmd_RobCo.char("| Computer system: " + var_RobCo.hostname)
    cmd_RobCo.char("\n| Computer system IP Address: " + var_RobCo.ipaddr)

    local_ip = os.popen('ipconfig getifaddr en0').read().strip()
    cmd_RobCo.char("\n| Local IP Address (en0): " + local_ip)

    public_ip = os.popen('curl -s ifconfig.me').read().strip()
    cmd_RobCo.char("\n| Public IP Address: " + public_ip)
    termS_RobCo.empty()

    func_RobCo.back(3, 6)


# cmd-terminal code
def cmd_main():
    termS_RobCo.robco_interface(print)

    termS_RobCo.header_("CMD TERMINAL", "-", cmd_RobCo.char)

    while True:
        cmd_RobCo.char("| [ctrl + C] to break command ")
        cmd_RobCo.char("| [BACK] ")
        cmd_RobCo.input_char("| > ")
        tDirectoryInput = input("")
        for char in ((os.system(tDirectoryInput)),):
            print(char, end='')
            sys.stdout.flush()
            time.sleep(0.01)
        sys_RobCo.log(3, 51, tDirectoryInput)

        if tDirectoryInput == "BACK":
            termS_RobCo.slide_up()

            func_RobCo.return_menu(3, 6)

            break


# contacts code
def contacts_main():
    termS_RobCo.robco_interface(print)

    termS_RobCo.header_("CONTACTS", "-", cmd_RobCo.char)

    while True:
        termS_RobCo.robco_interface(print)

        termS_RobCo.header_("CONTACTS", "-", print)
        contactChoice = ["Add new contact", "View contact", "Clear contact", "Return"]
        contact_choice_menu = TerminalMenu(contactChoice)
        contact_index = contact_choice_menu.show()
        entrySelection = contactChoice[contact_index]
        if entrySelection == "Add new contact":
            sys_RobCo.log(3, 55, "terminal-contacts")
            termS_RobCo.robco_interface(print)

            func_RobCo.add_entry(var_RobCo.contacts_dir)

            func_RobCo.back(3, 6)
        if entrySelection == "View contact":
            sys_RobCo.log(3, 53, "terminal-contacts")
            termS_RobCo.robco_interface(print)

            func_RobCo.view_entry(var_RobCo.contacts_dir)

            func_RobCo.back(3, 6)
        if entrySelection == "Clear contact":
            sys_RobCo.log(3, 19, "terminal-contacts")
            termS_RobCo.robco_interface(print)

            func_RobCo.clear_entry(var_RobCo.contacts_dir)

            func_RobCo.back(3, 6)
        if entrySelection == "Return":
            func_RobCo.return_menu(3, 6)

            break


# hack-sim code
def t_inquire_sim_main():
    while True:
        termS_RobCo.robco_interface(print)

        termS_RobCo.header_("HACKING/INQUIRE SIMULATOR", "-", cmd_RobCo.char)

        hackSimOptions = ["7 Letter word hack", "BACK"]
        hackSim_menu = TerminalMenu(hackSimOptions)
        hackSim_entry_index = hackSim_menu.show()
        hackSimSelection = hackSimOptions[hackSim_entry_index]
        if hackSimSelection == "7 Letter word hack":
            maint_RobCo.t_inquire_sim("system/sevenletterwords.txt")
        if hackSimSelection == "BACK":
            func_RobCo.return_menu(3, 6)

            break


# data archive code
def data_archive_main():
    termS_RobCo.robco_interface(print)

    termS_RobCo.header_("DATA ARCHIVE", "-", cmd_RobCo.char)
    while True:
        termS_RobCo.robco_interface(print)

        termS_RobCo.header_("DATA ARCHIVE", "-", print)
        entryChoice = ["Add new archive entry", "View archive entry", "Clear archive entry", "Return"]
        entry_choice_menu = TerminalMenu(entryChoice)
        entry_index = entry_choice_menu.show()
        entrySelection = entryChoice[entry_index]
        if entrySelection == "Add new archive entry":
            sys_RobCo.log(3, 55, "archive-entry")
            termS_RobCo.robco_interface(print)

            func_RobCo.add_entry(var_RobCo.archive_dir)

            func_RobCo.back(3, 6)
        if entrySelection == "View archive entry":
            sys_RobCo.log(3, 53, "archive-entry")
            termS_RobCo.robco_interface(print)

            func_RobCo.view_entry(var_RobCo.archive_dir)

            func_RobCo.back(3, 6)
        if entrySelection == "Clear archive entry":
            sys_RobCo.log(3, 19, "archive-entry")
            termS_RobCo.robco_interface(print)

            func_RobCo.clear_entry(var_RobCo.archive_dir)

            func_RobCo.back(3, 6)
        if entrySelection == "Return":
            func_RobCo.return_menu(3, 6)

            break


# system diagnostics code
def system_diagnostics_main():
    sys_RobCo.full_diagnostics(3, 6)


# system-logs code
def system_log_main():
    termS_RobCo.robco_interface(print)

    termS_RobCo.header_("SYSTEM LOG", "-", cmd_RobCo.char)
    termS_RobCo.slide_by_line('system/system-logs.log', delay=0.01)
    termS_RobCo.empty()

    func_RobCo.back(3, 6)


# 2
# settings code
def settings_menu():
    def clearance_m():
        while True:
            sys_RobCo.log(3, 47, "clearance_m")
            termS_RobCo.robco_interface(print)
            termS_RobCo.header_("SETTINGS", "-", print)

            clearanceOptions = ["View clearance", "Return"]
            clearance_menu = TerminalMenu(clearanceOptions)
            clearance_entry_index = clearance_menu.show()
            clearanceSelection = clearanceOptions[clearance_entry_index]
            if clearanceSelection == "View clearance":
                with open(var_RobCo.clearanceTXT, 'r') as f:
                    cmd_RobCo.char(f.read())
                    func_RobCo.back(3, 6)
            if clearanceSelection == "Return":
                func_RobCo.return_menu(3, 6)

                break

    def credentials_m():
        while True:
            sys_RobCo.log(3, 47, "cred_m")
            termS_RobCo.robco_interface(print)
            termS_RobCo.header_("SETTINGS", "-", print)

            credentialOptions = ["View credentials", "Change credentials", "Return"]
            credential_menu = TerminalMenu(credentialOptions)
            credential_entry_index = credential_menu.show()
            credentialsSelection = credentialOptions[credential_entry_index]
            if credentialsSelection == "View credentials":
                with open(var_RobCo.credTXT, 'r') as f:
                    cmd_RobCo.char(f.read())
                    func_RobCo.back(3, 6)
            if credentialsSelection == "Change credentials":
                with open(var_RobCo.credTXT, 'w') as F:
                    F.write("")
                    passwordEntry = input("> ")
                with open(var_RobCo.credTXT, 'a') as F:
                    F.write(passwordEntry)
                cmd_RobCo.char("Credentials changed to " + var_RobCo.credential)
                func_RobCo.back(3, 6)
            if credentialsSelection == "Return":
                func_RobCo.return_menu(3, 6)

                break

    def password_m():
        cmd_RobCo.char("ENTER PASSWORD NOW > ")
        passwordPASSWORD = e_RobCo.encoded_input("")
        try:
            stored_hashed_password = e_RobCo.read_password('user_info/password.txt')
        except FileNotFoundError:
            print("Password file not found. Please re-download password.txt from GitHub files password first.")
            return

        if e_RobCo.verify_password(passwordPASSWORD, stored_hashed_password):

            while True:
                sys_RobCo.log(3, 47, "password_m")
                termS_RobCo.robco_interface(print)

                termS_RobCo.header_("SETTINGS", "-", print)

                passwordOptions = ["View password", "Change password", "Return"]
                password_menu = TerminalMenu(passwordOptions)
                password_entry_index = password_menu.show()
                passwordSelection = passwordOptions[password_entry_index]
                if passwordSelection == "View password":
                    cmd_RobCo.char(f"Current password: {e_RobCo.read_password(var_RobCo.PasswordTXT)}")
                    func_RobCo.back(3, 6)
                if passwordSelection == "Change password":
                    passEntry = getpass("Enter your new password: ")
                    hashed_password = e_RobCo.encrypt_password(passEntry)
                    e_RobCo.store_password('user_info/password.txt', hashed_password)
                    print("Password stored successfully.")
                    termS_RobCo.empty()

                    cmd_RobCo.char(f"Password changed to: {passEntry}")
                    func_RobCo.back(3, 6)
                if passwordSelection == "Return":
                    func_RobCo.return_menu(3, 6)

                    break

    def username_m():
        while True:
            sys_RobCo.log(3, 47, "username_m")
            termS_RobCo.robco_interface(print)
            termS_RobCo.header_("SETTINGS", "-", print)

            usernameOptions = ["View username", "Change Username", "Return"]
            username_menu = TerminalMenu(usernameOptions)
            username_entry_index = username_menu.show()
            usernameSelection = usernameOptions[username_entry_index]
            if usernameSelection == "View username":
                with open(var_RobCo.UserTXT, 'r') as F:
                    cmd_RobCo.char(F.read())
                    func_RobCo.back(3, 6)
            if usernameSelection == "Change Username":
                with open(var_RobCo.UserTXT, 'w') as F:
                    F.write("")
                usernameEntry = input("> ")
                with open(var_RobCo.UserTXT, 'a') as F:
                    F.write(usernameEntry)
                cmd_RobCo.char("Username changed to " + usernameEntry)
                func_RobCo.back(3, 6)
            if usernameSelection == "Return":
                func_RobCo.return_menu(3, 6)

                break

    while True:
        termS_RobCo.robco_interface(print)

        termS_RobCo.header_("SETTINGS", "-", cmd_RobCo.char)

        cmd_RobCo.char("RobCoOS " + var_RobCo.softwareV)
        cmd_RobCo.char("ⓒ" + var_RobCo.year + " RobCo")
        termS_RobCo.empty()

        cmd_RobCo.char("SalliOS " + var_RobCo.salliV)
        cmd_RobCo.char(var_RobCo.ai)
        termS_RobCo.empty()
        termS_RobCo.empty()

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
            func_RobCo.return_menu(3, 6)

            break


# emergency protocols code
def emergency_protocols_main():
    termS_RobCo.robco_interface(print)

    termS_RobCo.header_("EMERGENCY PROTOCOLS", "-", cmd_RobCo.char)

    while True:
        termS_RobCo.robco_interface(print)
        termS_RobCo.header_("EMERGENCY PROTOCOLS", "-", print)
        emergencyChoice = ["New Emergency Protocols", "View Emergency Protocols", "Clear Emergency Protocols", "Return"]
        emergency_choice_menu = TerminalMenu(emergencyChoice)
        emergency_entry_index = emergency_choice_menu.show()
        emergencySelection = emergencyChoice[emergency_entry_index]
        if emergencySelection == "New Emergency Protocol":
            sys_RobCo.log(3, 55, "emergency-protocol")

            termS_RobCo.robco_interface(print)

            func_RobCo.add_entry(var_RobCo.emergencyProtocol_dir)

            func_RobCo.back(3, 6)
        if emergencySelection == "View Emergency Protocols":
            sys_RobCo.log(3, 53, "emergency-protocol")

            termS_RobCo.robco_interface(print)

            func_RobCo.view_entry(var_RobCo.emergencyProtocol_dir)

            func_RobCo.back(3, 6)
        if emergencySelection == "Clear Emergency Protocol":
            sys_RobCo.log(3, 19, "emergency-protocol")

            termS_RobCo.robco_interface(print)

            func_RobCo.clear_entry(var_RobCo.emergencyProtocol_dir)

            func_RobCo.back(3, 6)
        if emergencySelection == "Return":
            func_RobCo.return_menu(3, 6)

            break


# security ode
def security_main():
    def security_protocols():
        termS_RobCo.robco_interface(print)

        termS_RobCo.header_("SECURITY PROTOCOLS", "-", cmd_RobCo.char)

        while True:
            termS_RobCo.robco_interface(print)
            termS_RobCo.header_("SECURITY PROTOCOLS", "-", print)

            archiveChoice = ["New Security Protocol", "View Security Protocols", "Clear Security Protocol", "Return"]
            archive_choice_menu = TerminalMenu(archiveChoice)
            archive_entry_index = archive_choice_menu.show()
            archiveSelection = archiveChoice[archive_entry_index]
            if archiveSelection == "New Security Protocol":
                termS_RobCo.robco_interface(print)

                func_RobCo.add_entry(var_RobCo.protocols_dir)

                func_RobCo.back(3, 6)
            if archiveSelection == "View Security Protocols":
                termS_RobCo.robco_interface(print)

                func_RobCo.view_entry(var_RobCo.protocols_dir)

                func_RobCo.back(3, 6)
            if archiveSelection == "Clear Security Protocol":
                termS_RobCo.robco_interface(print)

                func_RobCo.clear_entry(var_RobCo.protocols_dir)

                func_RobCo.back(3, 6)
            if archiveSelection == "Return":
                func_RobCo.return_menu(3, 6)

                break

    def security_level():
        termS_RobCo.robco_interface(print)

        termS_RobCo.header_("SECURITY LEVEL", "-", cmd_RobCo.char)

        while True:
            termS_RobCo.robco_interface(print)
            securitylvlTXT = var_RobCo.securitylvlTXT
            securityrlvlTXT = var_RobCo.securityrlvlTXT
            termS_RobCo.header_("SECURITY LEVEL", "-", print)

            cmd_RobCo.char("Current Security Level : " + var_RobCo.securityLevel)
            cmd_RobCo.char("Security Level Reason  : " + var_RobCo.securityLvlRR)
            cmd_RobCo.char("Available Levels: ")
            termS_RobCo.empty()

            archiveChoice = ["Off", "Low", "Medium", "High", "BACK"]
            archive_choice_menu = TerminalMenu(archiveChoice)
            archive_entry_index = archive_choice_menu.show()
            archiveSelection = archiveChoice[archive_entry_index]
            if archiveSelection == "Off":
                termS_RobCo.robco_interface(print)

                with open(securitylvlTXT, 'w') as F:
                    F.write("")
                with open(securitylvlTXT, 'a') as F:
                    F.write("Off")
                cmd_RobCo.input_char("Security level reasoning: ")
                SlvlR = input("")
                with open(securityrlvlTXT, 'w') as F:
                    F.write("")
                with open(securityrlvlTXT, 'a') as F:
                    F.write(SlvlR)
            if archiveSelection == "Off":
                termS_RobCo.robco_interface(print)

                with open(securitylvlTXT, 'w') as F:
                    F.write("")
                with open(securitylvlTXT, 'a') as F:
                    F.write("LOW")
                cmd_RobCo.input_char("Security level reasoning: ")
                SlvlR = input("")
                with open(securityrlvlTXT, 'w') as F:
                    F.write("")
                with open(securityrlvlTXT, 'a') as F:
                    F.write(SlvlR)

                cmd_RobCo.char("SECURITY LEVEL UPDATED TO: LOW")

                func_RobCo.back(3, 6)
            if archiveSelection == "Medium":
                termS_RobCo.robco_interface(print)

                with open(securitylvlTXT, 'w') as F:
                    F.write("")
                with open(securitylvlTXT, 'a') as F:
                    F.write("HIGH")
                cmd_RobCo.input_char("Security level reasoning: ")
                SlvlR = input("")
                with open(securityrlvlTXT, 'w') as F:
                    F.write("")
                with open(securityrlvlTXT, 'a') as F:
                    F.write(SlvlR)

                cmd_RobCo.char("SECURITY LEVEL UPDATED TO: MEDIUM")

                func_RobCo.back(3, 6)
            if archiveSelection == "High":
                termS_RobCo.robco_interface(print)

                with open(securitylvlTXT, 'w') as F:
                    F.write("")
                with open(securitylvlTXT, 'a') as F:
                    F.write("HIGH")
                cmd_RobCo.input_char("Security level reasoning: ")
                SlvlR = input("")
                with open(securityrlvlTXT, 'w') as F:
                    F.write("")
                with open(securityrlvlTXT, 'a') as F:
                    F.write(SlvlR)

                cmd_RobCo.char("SECURITY LEVEL UPDATED TO: HIGH")

                func_RobCo.back(3, 6)
            if archiveSelection == "BACK":
                func_RobCo.return_menu(3, 6)

                break

    def security_logs_main():
        termS_RobCo.robco_interface(print)

        termS_RobCo.header_("SECURITY LOGS", "-", cmd_RobCo.char)

        while True:
            termS_RobCo.robco_interface(print)
            termS_RobCo.header_("SECURITY LOGS", "-", print)

            archiveChoice = ["New Security Entry", "View Security Entry", "Clear Security Entry", "BACK"]
            archive_choice_menu = TerminalMenu(archiveChoice)
            archive_entry_index = archive_choice_menu.show()
            archiveSelection = archiveChoice[archive_entry_index]
            if archiveSelection == "New Security Entry":
                termS_RobCo.robco_interface(print)

                func_RobCo.add_entry(var_RobCo.security_dir)

                func_RobCo.back(3, 6)
            if archiveSelection == "View Security Entry":
                termS_RobCo.robco_interface(print)

                func_RobCo.view_entry(var_RobCo.security_dir)

                func_RobCo.back(3, 6)
            if archiveSelection == "Clear Security Entry":
                termS_RobCo.robco_interface(print)

                func_RobCo.clear_entry(var_RobCo.security_dir)

                func_RobCo.back(3, 6)
            if archiveSelection == "BACK":
                func_RobCo.return_menu(3, 6)

                break

    termS_RobCo.robco_interface(print)

    termS_RobCo.header_("SECURITY SETTINGS", "-", cmd_RobCo.char)

    while True:
        termS_RobCo.robco_interface(print)
        termS_RobCo.header_("SECURITY SETTINGS", "-", print)

        protocolChoice = ["Security Logs", "Adjust Security Level", "Update Security Protocols", "Return"]
        protocol_choice_menu = TerminalMenu(protocolChoice)
        protocol_entry_index = protocol_choice_menu.show()
        protocolSelection = protocolChoice[protocol_entry_index]
        if protocolSelection == "Security Logs":
            sys_RobCo.log(3, 12, "security-logs")

            termS_RobCo.robco_interface(print)

            security_logs_main()
        if protocolSelection == "Adjust Security Level":
            sys_RobCo.log(3, 61, "security-level")

            termS_RobCo.robco_interface(print)

            security_level()
        if protocolSelection == "Update Security Protocols":
            sys_RobCo.log(3, 106, "security-protocols")

            termS_RobCo.robco_interface(print)

            security_protocols()
        if protocolSelection == "Return":
            func_RobCo.return_menu(3, 6)

            break


# maintenance code
def maintenance_main():
    def maintenance_log():
        while True:
            termS_RobCo.robco_interface(print)

            termS_RobCo.header_("MAINTENANCE REQUESTS/LOG", "-", print)
            cmd_RobCo.char("Maintenance Logs:")
            termS_RobCo.empty()

            maintChoice = ["Main Log", "Request Log", "Return"]
            maintChoice_menu = TerminalMenu(maintChoice)
            maint_entry_index = maintChoice_menu.show()
            selectionMaint = maintChoice[maint_entry_index]
            if selectionMaint == "Main Log":
                termS_RobCo.slide_by_line(var_RobCo.maintenanceLogTXT, delay=0.05)
                termS_RobCo.empty()
                func_RobCo.back(3, 6)

            if selectionMaint == "Request Log":
                termS_RobCo.slide_by_line(var_RobCo.maintenanceReqTXT, delay=0.05)
                termS_RobCo.empty()
                func_RobCo.back(3, 6)

            if selectionMaint == "Return":
                func_RobCo.return_menu(3, 6)
                break

    def maintenance_req():
        termS_RobCo.robco_interface(print)

        termS_RobCo.header_("MAINTENANCE REQUESTS/LOG", "-", print)
        cmd_RobCo.input_char("New request: ")
        requestM = input("")
        with open(var_RobCo.maintenanceReqTXT, 'a') as File:
            File.write(f"New Maintenance Request: {requestM}\n")
        func_RobCo.back(3, 6)

    while True:
        termS_RobCo.robco_interface(print)

        termS_RobCo.header_("MAINTENANCE REQUESTS/LOG", "-", cmd_RobCo.char)
        termS_RobCo.empty()

        choice = ["View Maintenance Logs", "Request a Maintenance Log", "Return"]
        choice_menu = TerminalMenu(choice)
        entry_index = choice_menu.show()
        selection = choice[entry_index]
        if selection == "View Maintenance Logs":
            maintenance_log()
        if selection == "Request a Maintenance Log":
            maintenance_req()
        if selection == "Return":
            func_RobCo.return_menu(3, 6)

            break


# restart code
def restart_menu():
    termS_RobCo.robco_interface(print)

    termS_RobCo.header_("RESTART", " ", cmd_RobCo.char)

    restartopt = ["Confirm", "Return"]
    restartopt_menu = TerminalMenu(restartopt)
    restartopt_index = restartopt_menu.show()
    restart_selection = restartopt[restartopt_index]
    if restart_selection == "Confirm":
        python = sys.executable
        os.execl(python, python, *sys.argv)
    elif restart_selection == "Return":
        cmd_RobCo.char("Returning")


# shutdown code
def shutdown_menu():
    termS_RobCo.header_("SHUTDOWN MENU", " ", cmd_RobCo.char)

    shutDownOptions = ["Confirm", "Abort"]
    shutDownC_menu = TerminalMenu(shutDownOptions)
    shutDown_entry_index = shutDownC_menu.show()
    shutDownChoice = shutDownOptions[shutDown_entry_index]
    if shutDownChoice == "Confirm":
        sys_RobCo.log(3, 72, "")
        termS_RobCo.slide_up()

        cmd_RobCo.clear()

        func_RobCo.exit_info("SHUTTING DOWN")

        # Shuts down Operating System / Computer for Linux/Apple
        os.system("sudo shutdown -h now")
    if shutDownChoice == "Abort":
        sys_RobCo.log(3, 73, "")
        cmd_RobCo.char("| Shutdown aborted")
        func_RobCo.return_menu(3, 7)


# exit code
def exit_menu():
    cmd_RobCo.clear()

    termS_RobCo.empty()

    sys_RobCo.log(3, 14, "")
    func_RobCo.exit_info("POWERING OFF TERMINAL")
    exit()
