import re
import subprocess


def get_my_mac(interface="en0"):  # en0 = WiFi on most Macs
    out = subprocess.check_output(["ifconfig", interface], text=True)
    match = re.search(r"ether ([0-9a-f:]{17})", out)
    return match.group(1) if match else None


print(get_my_mac())
