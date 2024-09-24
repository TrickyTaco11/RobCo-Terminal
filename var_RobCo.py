from datetime import *
import platform
import socket
import os

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

maintenanceLogTXT = 'system/maintenance/maintenance-log.txt'
maintenanceReqTXT = 'system/maintenance/maintenance-requests.txt'

# Reading txt
with open(UserTXT, "r") as userFile:
    user = userFile.readline().strip("\n")

with open(PasswordTXT, "rb") as file:
    encrypted_password_from_file = file.read()

with open(credTXT, "r") as credFile:
    credential = credFile.readline().strip("\n")

with open(clearanceTXT, "r") as clearanceFile:
    clearance = clearanceFile.readline().strip("\n")

with open(securitylvlTXT, "r") as securityLvlFile:
    securityLevel = securityLvlFile.readline().strip("\n")

with open(securityrlvlTXT, "r") as securityLvlRRFile:
    securityLvlRR = securityLvlRRFile.readline().strip("\n")

with open(maintenanceLogTXT, 'r') as maintenanceLOGFile:
    maintenanceLog = maintenanceLOGFile.readline().strip("\n")

with open(maintenanceLogTXT, 'r') as maintenanceREQFile:
    maintenanceReq = maintenanceREQFile.readline().strip("\n")

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

maintenance_dir = "maintenance"
os.makedirs(maintenance_dir, exist_ok=True)

contacts_dir = "contacts"
os.makedirs(contacts_dir, exist_ok=True)

# Paths
paths = [
    'archive_entries',
    'emergency_protocols',
    'error_codes',
    'contacts',
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
    'e_RobCo.py',
    'mainCode_RobCo.py',
    'maint_RobCo.py',
    'cmd_RobCo.py',
    'func_RobCo.py',
    'sys_RobCo.py',
    'termS_RobCo.py',
    'var_RobCo.py',
]
directoryB_paths = ["archive_entries", "emergency_protocols", "error_codes", "journal_entries", "security_level",
                    "security_logs", "security_logs", "security_protocols", "system", "user_info", "venv"]

# Settings
centre = 95
progressI = "- IN PROGRESS - ".center(centre, "-")

# System
softwareV = "v4.2"
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

# os
current_os = platform.system()

# Chars
GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'
