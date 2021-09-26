import string,os
from ctypes import windll

main_name_dir="Condor"
TOKEN = "INSERT TELEGRAM TOKEN"

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives



def processing():
    list_drives_connected=get_drives()
    for label in list_drives_connected:
        if label != "C":
            for root, dirs, files in os.walk(f"{label}:\\"):
                if "Condor.py" in files or "Condor" in files:
                    label_disk=f"{label}:\\"
                    return label_disk



