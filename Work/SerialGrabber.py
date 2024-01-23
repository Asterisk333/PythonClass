# wmic bios get serialnumber#Windows
# hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid#Linux
# ioreg -l | grep IOPlatformSerialNumber#Mac OS X
import os
import sys


def getMachine_addr():
    serialnumber = None


    os_type = sys.platform.lower()
    if "win" in os_type:
        command = "wmic bios get serialnumber"
    elif "linux" in os_type:
        #  find a way to get all serial number
        command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
    elif "darwin" in os_type:
        command = "ioreg -l | grep IOPlatformSerialNumber"
    return os.popen(command).read().replace("\n", "").replace("  ", "").replace("SerialNumber", "SerialNumber: ").strip()
    #  possible to do the return statement in the call of os?
    #return serialnumber[0] + ": " + serialnumber[1]


# output machine serial code: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX
print(getMachine_addr())
