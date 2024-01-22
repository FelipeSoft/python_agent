import psutil
import time
import platform
from utils import get_lines_stdout, format_bits_to_gigabytes, get_random_memory_type
import subprocess


# Need a constant update every second
def get_cpu_usage():
    cpu = psutil.cpu_percent(interval=1)
    return cpu


def get_ram_usage():
    ram = psutil.virtual_memory().percent
    return ram


# Doesn't need a constant update every second
def get_multiplatform_hardware_info():
    output = {
        "os": platform.system(),
        "machine": platform.machine(),
        "platform": platform.platform(),
        "processor": platform.processor()
    }
    return output


def get_multiplatform_network_connections():
    output = []
    for connection in psutil.net_connections():
        remote_address = []
        if connection.raddr and connection.raddr.ip and connection.raddr.port:
            remote_address = [connection.raddr.ip, connection.raddr.port]

        local_address = [connection.laddr.ip, connection.laddr.port]

        output.append({
            "status": connection.status,
            "pid": connection.pid,
            "fd": connection.fd,
            "remote_address": remote_address,
            "local_address": local_address
        })

    return output


def get_windows_services():
    output = []
    for process in psutil.process_iter():
        if process.name().lower().startswith("svchost.exe"):
            output.append({
                "pid": process.pid,
                "status": process.status()
            })

    return output


def get_windows_random_memory():
    command = "wmic memorychip get Capacity, Manufacturer, MemoryType, PartNumber, SerialNumber"
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        output = get_lines_stdout(result.stdout)
        for r in output:
            r["Capacity"] = format_bits_to_gigabytes(r["Capacity"])
            r["MemoryType"] = get_random_memory_type(r["MemoryType"])

        return output


def get_multiplatform_processes():
    output = []
    for process in psutil.process_iter():
        output.append({
            "pid": process.pid,
            "name": process.name(),
            "status": process.status()
        })

    return output


def has_backup(processes):
    for process in processes:
        if "grpm" in process.get("name").lower():
            return True


def has_antivirus(processes):
    for process in processes:
        if ("protect" in process.get("name").lower()) or ("antivirus" in process.get("name").lower()):
            return True


print(get_windows_random_memory())

