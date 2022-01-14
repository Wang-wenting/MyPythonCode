import subprocess
import ctypes, sys
import os
cmd = "net user test3 123456 /add"


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("以管理员权限运行")
    # 杀掉名字为Au_.exe的进程
    os.system(r"time 0:0:0.0")
else:
    if sys.version_info[0] == 3:
        print("无管理员权限")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)