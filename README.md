# RobCo-Terminal
A Fallout, RobCo style terminal emulator (like) script for python3.

Welcome to the ROBCO INDUSTRIES (TM) TERMLINK! This terminal emulator is inspired by the iconic terminals from the Fallout series of video games. This application allows you to manage passwords, usernames, view system logs, handle error directories, manage security, perform hacking activities, and view entry logs with a vintage terminal script.

I recommend using 'Cool-retro-term' by Swordfish90: https://github.com/Swordfish90/cool-retro-term/tree/1.2.0

The centre of the screen for the script is set in the 'Terminal.py' file line: 173.

## Features

- **User Management**: View and change passwords, usernames, credentials, authorisation.
- **System Log**: Logs every move you make so you are able to view at anytime, you can also reset the system log.
- **Error Directory**: Display a list of error codes from the fallout series.
- **Security Management**: Manage security settings and security logs.
- **Hacking Interface**: Simulate hacking attempts with fallouts retro-style interface.
- **Entry Logs**: View, create and clear entry logs just as you would in fallout.
- **Help Menu**: Get instructions and information about using the terminal.
- **Exit**: Safely exit the terminal application.

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/TrickyTaco11/RobCo-Terminal.git
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

Upon running the script, you will be in a small section of the terminal where simple commands (still in progress) can be prompted... type 'help' for a list of commands (some may not function correctly). You can login on that same command line, once authenticated, you can navigate through various menus to manage entries, a custom missile silo inventory system, usernames, passwords, system logs, a normal terminal function, security settings, and perform hacking activities.

The custom missile system is a .txt file with a graph of missile silo inventories for each countries, all data is recieved from: : https://www.armscontrol.org/factsheets/missiles
This is there just for aesthetics, not functional in anyway except for viewing different missile variants in specified countries (all public information).

### Main Menu Commands
Some of the main menu commands:

**Settings**:
- **Password**: View or change your password.
- **Username**: View or change your username.
- **Credential**: View or change your credentials.
- **Clearance**: View your clearance (overseer, admin, ect...), which can be altered in the clearance.txt file

**System Logs**:
- **View system-logs**: Displays the system logs.
- **Set terminal/system_logs**: Resets or clears the system logs.

**Error Directory**:
- **View error_dir**: Displays a list of error codes from various files.

**Security Management**:
- **Security settings**: Displays current security settings.
- **Modify security levels**: Allows modification of security levels with a reason.
- **Security logs**: Change/add and displays logs of security-related events.

**Hacking Interface**:
- **Simulate hacking attempts**: Provides an interactive hacking simulation.

**Entry Logs**:
- **Manage entry logs**: Allows management (viewing, adding, deleting) of entry logs just like the Fallout Series.

**Data Archive**:
- **Experiments**: Just like the entry-logs but instead is entirely dedicated to expermentation data and logs.

**Help Menu**:
- **Help**: Displays instructions, command-lines and information about using the terminal system.

**Terminal**:
- **Terminal**: Able to use your regular operating systems terminal from within the script.

**Exit/restart**: 
- **Exit**: Exits the terminal application.
- **Restart**: Restarts the OS or terminal.py.
- **Logout**: Able to logout of the main terminal, back into the basic command terminal.

**Hack into Terminal**:
- **Hacking**: You can simply hack into the terminal if you do not have the log in. You can use Fallout-3 'set terminal/inquire' command in the specified capslock on the terminal system to prompt the hacking all Fallout fans know. 

### Notes

- The terminal interface is designed to replicate the feel of the Fallout 3 & 4 computer-terminal systems.
- Saves are automatic once the file has been created. eg/: if you write an entry; you just have to finish writing in it and press 'enter' for it to save automatically. If your computer turns off during writing or the scirpt is cancelled, there may be a possibility that the file may not be upto date, or written at all.
- This is a work in progress, I am not an experienced programmer. I was simply doing this for fun since I owned an old CRT display and wanted to create a Fallout Series terminal.

## Contributing

If you wish to contribute to the project, please fork the repository and submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License.

---

Enjoy using the ROBCO INDUSTRIES (TM) TERMLINK and feel free to report any issues or suggest features to improve the application.
