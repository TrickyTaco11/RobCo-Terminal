# Instructions Manual

This instruction manual should surely help you understand the basics, and the advanced of the RobCo Terminal and its functions. This file will be updated 

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/TrickyTaco11/RobCo-Terminal.git
   ```
   ^^ or download the code / release!
2. **Install the Libraries**:
   ```
   pip install simple-term-menu
   ```
   ```
   pip install subprocess
   ```
   ```
   pip install datetime
   ```
   ```
   pip install platform
   ```
   ```
   pip install logging
   ```
   ```
   pip install getpass
   ```
   ```
   pip install shutil
   ```
   ```
   pip install socket
   ```
   ```
   pip install random
   ```
   ```
   pip install string
   ```
   ```
   pip install bcrypt
   ```
   ```
   pip install getch
   ```
   ```
   pip install time
   ```
   ```
   pip install sys
   ```
   ```
   pip install os
   ```
4. **Navigate to the project directory**:
   ```
   cd path/to/RobCo-Terminal-4.0
   ```
5. **Run the terminal application**:
   ```
   python3 terminal.py
   ```

## Running the script
As soon as you run the script you will be prompted with a brief loading screen which checks the directories and essential files.
After, you will be prompted with a basic terminal. 
<img width="1068" alt="Screenshot 2024-07-31 at 9 43 12 AM" src="https://github.com/user-attachments/assets/55e41cea-fe06-4d64-8f54-b6bfa921a882">
In this terminal you can prompt simple commands; a list of commands are shown when you prompt: 'help'.
<img width="1068" alt="Screenshot 2024-07-31 at 9 51 25 AM" src="https://github.com/user-attachments/assets/a794772b-f121-4210-9e32-03c310dc724e">


In this basic terminal you can logon to the main admin terminal via prompting: 'logon (username)', this will then ask you for your password displayed in hashes(*).
The logon and password are automatically set to 'admin' and '1234'.
<img width="1065" alt="Screenshot 2024-07-31 at 9 53 15 AM" src="https://github.com/user-attachments/assets/cc0fd9fe-5708-4d4b-9433-4a9133ba47fb">
OR you can hack your way in by typing the prompt below!
<img width="1068" alt="Screenshot 2024-07-31 at 9 56 36 AM" src="https://github.com/user-attachments/assets/dd7e2efe-67d0-4308-be79-0aa87f197598">

After you have logged in you will be sent to the 'Admin Portal'. This is where you can access entry logs, settings, security, your regular OS-Terminal, system-logs, and a lot more. 
<img width="1067" alt="Screenshot 2024-07-31 at 9 58 48 AM" src="https://github.com/user-attachments/assets/5a106713-f48e-471a-80c8-9bd18e3a589b">

I will show you an example of using the terminal Entry Log; this works the same for the Data Archive, Security Logs and Emergency Protocols.
In each of these you can, create, view and clear different terminal entries.

## Entry Logs
***Entry Log***
This is the entry log main page, here you can access all the different options.
<img width="1061" alt="Screenshot 2024-07-31 at 10 42 04 AM" src="https://github.com/user-attachments/assets/09c8ffb0-bf12-4b68-87ab-d6a6698b49d6">

***Add Entry***
You will be asked for a title for your entry, followed by the actual entry you wish to create. This will save as a .txt file in the journal_entries directory.
<img width="1066" alt="Screenshot 2024-07-31 at 10 44 58 AM" src="https://github.com/user-attachments/assets/0972ea2a-87f1-4523-a5d0-a73f2c871ca1">

***View Entry***
From here you can view any entry you have created.


<img width="288" alt="Screenshot 2024-07-31 at 10 45 32 AM" src="https://github.com/user-attachments/assets/c98abca6-189f-403b-bb85-f7f7813bff89">
<img width="1067" alt="Screenshot 2024-07-31 at 10 45 38 AM" src="https://github.com/user-attachments/assets/d3135668-27a2-43dd-9814-882bd546c3fc">

***Clear Entry***
From here you will be asked to select an entry to delete, followed by a confirmation. If you wish to not delete any entries; click on any entry then clicke 'No', this will return you to the entry log menu.


<img width="333" alt="Screenshot 2024-07-31 at 10 46 19 AM" src="https://github.com/user-attachments/assets/68806d50-8c78-41fe-a2cd-0ce2179ace8b">
<img width="473" alt="Screenshot 2024-07-31 at 10 46 25 AM" src="https://github.com/user-attachments/assets/60e4e713-edaf-4511-9390-73ac7bc17bcc">


## System Logs
The system-log is a log file that tracks every movement you make (i.e. if you pressed a return button, it will show in the log that you did. If you accessed your settings it will log it as is.). Some sections are redacted from the log like the password section of the settings, it will show that it has been 'protected:sys(setting)', this is for privacy reasons. This file can be cleared/reset using; 'set terminal/system-logs' ENTER, then: set 'file/overwrite=clear'.


## System Diagnostics
In this you will be able to see your CPU usage, Memory, Hard drive, Network and Power supply. You are also given an error log, which scans your computer for errors and logs them as so. 

<img width="1066" alt="Screenshot 2024-07-31 at 1 50 50 PM" src="https://github.com/user-attachments/assets/f48dce29-74bb-4fe1-adad-da2059c38030">

You are also given a menu of choices to choose from:
<img width="1059" alt="Screenshot 2024-07-31 at 1 50 59 PM" src="https://github.com/user-attachments/assets/59597665-a827-4ffd-9e2f-13210d734a25">

**View System Performance Report**:
<img width="1059" alt="Screenshot 2024-07-31 at 1 54 26 PM" src="https://github.com/user-attachments/assets/1323dd4c-4f3a-4bdb-9685-d638c460996b">
This provides you with your CPU Usage and Memory Usage. 

**Backup Data**:
This option will back-up all of your directories and files within the Terminalv(x), these will be backed up and moved to a new directory labeled 'backup_data'. This will keep and save your work, these can be accessed using 'view p- path/to/file' in the basic terminal.

**Reboot System**:
This option will reboot your operating-system. Your full computer.


## Contacts
Contacts is currently a work in progress.
This feature in theory; will allow other users running the Terminal script to communicate between one another. This will also allow people to send and recieve emails from one-another, acting as your mail library.

## RESTART
The restart function on the Admin Portal allows users to prompt a quick re-log on the project without having to sign back in.

## Contributing

If you wish to contribute to the project, please fork the repository and submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License.

---

Enjoy using the ROBCO INDUSTRIES (TM) TERMLINK and feel free to report any issues or suggest features to improve the application.
