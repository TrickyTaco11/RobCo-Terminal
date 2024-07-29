# RobCo-Terminal
A Fallout, RobCo style terminal emulator (like) script for python3.

Welcome to the ROBCO INDUSTRIES (TM) TERMLINK! This terminal emulator is inspired by the iconic terminals from the Fallout series of video games. This application allows you to manage passwords, usernames, view system logs, handle error directories, manage security, perform hacking activities, and view entry logs with a vintage terminal script.

I recommend using 'Cool-retro-term' by Swordfish90: https://github.com/Swordfish90/cool-retro-term/tree/1.2.0

The centre of the screen for the script is set in the 'Terminal.py' file line: 173.
The current centerLine is set to 95, this is because that is the size of my CRT display.

The logon is set to 'admin' with the password being '1234' this can be changed in the settings section of the admin menu. I will be creating a more advanced encrypted password.txt file so no one can open the file and see the password clear as day. I am currently working on the encryption!

## Key Features

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

### Pictures
**Loading Screen**
<img width="1075" alt="Screenshot 2024-07-29 at 11 22 19 AM" src="https://github.com/user-attachments/assets/33dcfe57-4283-4aa7-b86a-b775572e0b4e">

**Logon**
<img width="1074" alt="Screenshot 2024-07-29 at 11 26 24 AM" src="https://github.com/user-attachments/assets/34604ce6-fed6-4de8-bbc8-9fe41da8ea3a">

**Hacking**
<img width="1077" alt="Screenshot 2024-07-29 at 11 24 59 AM" src="https://github.com/user-attachments/assets/7137f539-ff08-4aff-abde-109e72760d82">

**Admin Menu**
<img width="1077" alt="Screenshot 2024-07-29 at 11 25 29 AM" src="https://github.com/user-attachments/assets/a94bc1d2-8220-4b62-99b0-b5e284812b8f">

**Normal Menu 'Help'**
<img width="1074" alt="Screenshot 2024-07-29 at 11 26 24 AM" src="https://github.com/user-attachments/assets/2fbefe46-7586-4c14-ac33-154657c81e09">


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
- There are still some bugs and 'IN PROGRESS' sections to this project, the code may not be the fanciest but it works for the time being, I will clean up the code for every major version released.

## Contributing

If you wish to contribute to the project, please fork the repository and submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License.

---

Enjoy using the ROBCO INDUSTRIES (TM) TERMLINK and feel free to report any issues or suggest features to improve the application.
