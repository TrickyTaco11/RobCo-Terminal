# RobCo-Terminal
A Fallout, RobCo style terminal emulator (like) script for python3.

Welcome to the ROBCO INDUSTRIES (TM) TERMLINK! This terminal emulator is inspired by the iconic terminals from the Fallout series of video games. This application allows you to manage passwords, usernames, view system logs, handle error directories, manage security, perform hacking activities, and view entry logs with a vintage terminal script.

I recommend using 'Cool-retro-term' by Swordfish90: https://github.com/Swordfish90/cool-retro-term/tree/1.2.0

The centre of the screen for the script is set in the Terminal.py file line: 168.

## Features

- **Password Management**: View and change the terminal password.
- **Username Management**: View and change the terminal username.
- **System Logs**: View and reset system logs.
- **Error Directory**: Display a list of error codes from various files.
- **Security Management**: Manage security settings and logs.
- **Hacking Interface**: Simulate hacking attempts with a retro-style interface.
- **Entry Logs**: View and manage entry logs.
- **Help Menu**: Get instructions and information about using the terminal.
- **Exit**: Safely exit the terminal application.

## Installation

1. **Clone the repository**:
   ```
   [git clone https://github.com/TrickyTaco11/RobCo-Terminal.git]
   (https://github.com/TrickyTaco11/RobCo-Terminal.git)
   ```
2. **Navigate to the project directory**:
   ```
   cd RobCo-Terminal
   ```
3. **Run the terminal application**:
   ```
   python3 terminal.py
   ```

## Usage

Upon running the script, you will be in a small section of the terminal where simple commands (still in progress) can be prompted... type 'help' for a list of commands (some may not function correctly). You can login on that same command line, once authenticated, you can navigate through various menus to manage entries, a custom missile silo inventory system: getting information from: https://www.armscontrol.org/factsheets/missiles, usernames, passwords, system logs, a normal terminal function, security settings, and perform hacking activities.

### Main Menu Commands
Some of the main menu commands:

- **Password Management**:
- **View password**: Displays the current password.
- **Change password**: Prompts to enter a new password and saves it.

- **Username Management**:
- **View username**: Displays the current username.
- **Change Username**: Prompts to enter a new username and saves it.

- **System Logs**:
- **View system-logs**: Displays the system logs.
- **Set terminal/system_logs**: Resets or clears the system logs.

- **Error Directory**:
- **View error_dir**: Displays a list of error codes from various files.

- **Security Management**:
- **View security settings**: Displays current security settings.
- **Modify security settings**: Allows modification of security settings.
- **View security logs**: Displays logs of security-related events.

- **Hacking Interface**:
- **Simulate hacking attempts**: Provides an interactive hacking simulation.

- **Entry Logs**:
- **View entry logs**: Displays logs of entries made into the system.
- **Manage entry logs**: Allows management (viewing, adding, deleting) of entry logs.

- **Help Menu**:
- **help**: Displays instructions and information about using the terminal.

- **Exit**: Exits the terminal application.

### Detailed Functionality

#### Password Management
- **password_m()**: This function manages password-related tasks.
- **View password**: Reads and displays the current password from `PasswordTXT`.
- **Change password**: Prompts for a new password, writes it to `PasswordTXT`, and confirms the change.

#### Username Management
- **username_m()**: This function manages username-related tasks.
- **View username**: Reads and displays the current username from `UserTXT`.
- **Change Username**: Prompts for a new username, writes it to `UserTXT`, and confirms the change.

#### System Logs
- **sys_log2**: Logs system events with a timestamp and context.
- **view system-logs**: Displays the current system logs by reading `system-logs.txt`.
- **set terminal/system_logs**: Resets the system logs, clearing the `systemLogTXT` file and starting fresh.

#### Error Directory
- **view error_dir**: Displays a list of predefined error codes and descriptions from files in the error directory.
- Files include: `0x0AABFF00.txt`, `0x0D890102.txt`, etc.

#### Security Management
- **View security settings**: Displays current security settings from `security.txt`.
- **Modify security settings**: Prompts to modify and save new security settings to `security.txt`.
- **View security logs**: Displays security logs from `security-logs.txt`.

#### Hacking Interface
- **Simulate hacking attempts**: Provides an interactive hacking simulation similar to the mini-games found in Fallout, allowing users to attempt hacking into the system.

#### Entry Logs
- **View entry logs**: Displays logs of entries made into the system from `entry-logs.txt`.
- **Manage entry logs**: Allows adding new entries, viewing existing entries, and deleting specific entries from `entry-logs.txt`.

#### Help Menu
- **help_m()**: Displays a help menu with instructions or information by reading `help-menu.txt`.

#### Exiting
- **exit**: Logs the exit event and terminates the application.

### Notes

- The terminal interface is designed to replicate the feel of vintage computer systems.
- Make sure to save your changes before exiting the application to avoid losing any updates.

## Contributing

If you wish to contribute to the project, please fork the repository and submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License.

---

Enjoy using the ROBCO INDUSTRIES (TM) TERMLINK and feel free to report any issues or suggest features to improve the application.
