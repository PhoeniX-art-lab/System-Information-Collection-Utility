import wmi
import tkinter as tk
import subprocess
from win32api import GetSystemMetrics

# print(platform.uname())
# current_major_version = wmi.WMI().Win32_OperatingSystem()[0].Caption.encode("ascii", "ignore").decode("utf-8")
# print(current_major_version)
# print(os.environ.get("USERNAME"))
# print(platform.architecture())
# print(cpuinfo.get_cpu_info())

# print(wmi.WMI().Win32_DiskDrive()[0])             # ROM
# print(wmi.WMI().Win32_OperatingSystem()[0])       # OS
# print(wmi.WMI().Win32_VideoController()[0])       # GPU
# print(wmi.WMI().Win32_BaseBoard()[0])             # Base Board
# print(wmi.WMI().Win32_DesktopMonitor()[0])        # Monitor
# print(wmi.WMI().Win32_Processor()[0])             # CPU
# print(wmi.WMI().CIM_VideoControllerResolution()[0])
# print(wmi.WMI().CIM_VideoSetting()[0])
# print(wmi.WMI().Win32_SoundDevice()[0])            # Audio
# print(wmi.WMI().Win32_BIOS()[0])                    # BIOS


# direct_output = subprocess.check_output('powershell [uint64]"0x180000000"/1073741824', shell=True).decode('utf-8')
# print(direct_output)

# direct_output = subprocess.check_output('wmic path win32_VideoController get AdapterRAM, Name', shell=True)
# res = ''
# for i in range(len(direct_output)):
#     res += chr(direct_output[i])
#
# print(res)
# res = res.split('  ')
# for i in range(len(res)):
#     res[i] = res[i].replace('\r', '')
#     res[i] = res[i].replace('\n', '')
#     res[i] = res[i].replace(' ', '')
# while True:
#     try:
#         res.remove('')
#     except ValueError:
#         break
#
# print(res)

from information import *


class Test(Information):
    def __init__(self):
        super(Test, self).__init__()
        self.my = self.computer_text

    def printing(self):
        print(self.my)


a = Test()
a.printing()
