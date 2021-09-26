#!/usr/bin/python3

import subprocess
import platform
 
f = open('/home/USER/status.txt', 'r+')
f.truncate(0)
f.close()

f = open('/home/USER/status.txt', 'a')


def ping_ip(Allsky_ip):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
            ) == "windows" else 'c', Allsky_ip ), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False
 
if __name__ == '__main__':
    Allsky_ip = ['allsky.local']
    for each in Allsky_ip:
        if ping_ip(each):
            f.write(f"Allsky Online"+'\n')
        else:
            f.write(f"Allsky Offline"+'\n')
    f.close()
