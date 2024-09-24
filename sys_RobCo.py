import logging
import platform
import socket
import os

import func_RobCo
import var_RobCo
import cmd_RobCo
import termS_RobCo


# ----- System logs
def m_log(code_number, if_input):
    logging.info("* $RobCo_OS:  system:" + cmd_RobCo.read_specific_line("system/system-codes-for-log.txt", code_number)
                 + if_input)


def log(space_amount, code_number, if_input):
    space = "   " * space_amount + "* "
    logging.info("* $RobCo_OS:  system:" + space + cmd_RobCo.read_specific_line("system/system-codes-for-log.txt",
                                                                                code_number) + if_input)


def e_log():
    with open(var_RobCo.systemLogLOG, 'a') as F:
        F.write(" \n")
    with open(var_RobCo.systemLogLOG, 'a') as F:
        F.write("=".center(var_RobCo.centre, "=") + "\n")
    with open(var_RobCo.systemLogLOG, 'a') as F:
        F.write(" \n")


# ----- Error Codes
def list_error():
    log(1, 12, "error_dir")
    cmd_RobCo.char("ALL ERROR CODES RobCo_OS Terminal:")
    termS_RobCo.empty()

    termS_RobCo.slide_by_line("error_codes/0x0AABFF00.txt", delay=0.02)
    termS_RobCo.slide_by_line("error_codes/0x0D890102.txt", delay=0.02)
    termS_RobCo.slide_by_line("error_codes/0x00B636C6.txt", delay=0.02)
    termS_RobCo.slide_by_line("error_codes/0x03C663A1.txt", delay=0.02)
    termS_RobCo.slide_by_line("error_codes/0x07F6BAAC.txt", delay=0.02)
    termS_RobCo.slide_by_line("error_codes/0x357C5001.txt", delay=0.02)
    termS_RobCo.slide_by_line("error_codes/0x00001001.txt", delay=0.02)
    termS_RobCo.slide_by_line("error_codes/0x00001011.txt", delay=0.02)
    termS_RobCo.slide_by_line("error_codes/0xA001C007.txt", delay=0.02)
    termS_RobCo.slide_by_line("error_codes/0xF141A013.txt", delay=0.02)
    termS_RobCo.slide_by_line("error_codes/0xFA770171.txt", delay=0.02)
    termS_RobCo.slide_by_line("error_codes/0xFFF11011.txt", delay=0.02)
    termS_RobCo.slide_by_line("system/corrupt-error.txt", delay=0.02)


# ----- Diagnostics
# 1. Operating System Information
def os_info():
    termS_RobCo.header_(" Operating System Information ", "-", print)
    _os_info = platform.uname()
    cmd_RobCo.char(f"System: {_os_info.system}\n")
    cmd_RobCo.char(f"Node Name: {_os_info.node}\n")
    cmd_RobCo.char(f"Release: {_os_info.release}\n")
    cmd_RobCo.char(f"Version: {_os_info.version}\n")
    cmd_RobCo.char(f"Machine: {_os_info.machine}\n")
    cmd_RobCo.char(f"Processor: {_os_info.processor}\n")


# 2. CPU Information (Using sysctl command on macOS)
def cpu_info():
    termS_RobCo.header_(" CPU Information ", "-", print)
    cpu_info = os.popen("sysctl -n machdep.cpu.brand_string").read().strip()
    cmd_RobCo.char(f"CPU: {cpu_info}\n")

    cmd_RobCo.char("\nCPU Usage:\n")
    cpu_usage = os.popen("top -l 1 | grep 'CPU usage'").read().strip()
    cmd_RobCo.char(f"{cpu_usage}\n")


# 3. Memory Information (Using vm_stat on macOS)
def memory_info():
    termS_RobCo.header_(" Memory Information ", "-", print)
    vm_stat = os.popen("vm_stat").readlines()
    cmd_RobCo.char(f"Memory Stats:\n")
    for stat in vm_stat:
        cmd_RobCo.char(stat)


# 4. Disk Information (Using df -h for Disk Usage)
def disk_info():
    termS_RobCo.header_(" Disk Information ", "-", print)
    disk_usage = os.popen("df -h").read().strip()
    cmd_RobCo.char(f"{disk_usage}\n")


# 5. Network Information (Using ifconfig and curl for IP)
def network_info():
    termS_RobCo.header_(" Network Information ", "-", print)
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    cmd_RobCo.char(f"Hostname: {hostname}\n")
    cmd_RobCo.char(f"Local IP Address: {local_ip}\n")

    # Public IP using external service
    try:
        public_ip = os.popen("curl -s ifconfig.me").read().strip()
        cmd_RobCo.char(f"Public IP Address: {public_ip}\n")
    except Exception as e:
        cmd_RobCo.char(f"Could not retrieve Public IP Address: {e}\n")


# 6. Battery Information (Using system_profiler for battery data on macOS)
def battery_info():
    termS_RobCo.header_(" Battery Information ", "-", print)
    battery__info = os.popen("pmset -g batt").read().strip()
    cmd_RobCo.char(f"{battery__info}\n")


# Full diagnostics function
def full_diagnostics(a, b):
    os_info()
    cpu_info()
    memory_info()
    disk_info()
    network_info()
    battery_info()
    func_RobCo.back(a, b)
