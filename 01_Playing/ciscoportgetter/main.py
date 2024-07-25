import paramiko
import socket

from dotenv import load_dotenv
import os


class SwitchData:
    def __init__(self, data):
        self.data = [item for item in data.split(" ") if item]


class CoreSwitchData(SwitchData):
    def __init__(self, data):
        super().__init__(data)
        self.ipaddress = self.data[1]
        self.macaddress = self.data[3]
        self.vlan = self.data[5].strip()
        self.switch = self.vlan[-2:]

    def show_data(self):
        print(f"IP: {self.ipaddress} | MAC: {self.macaddress} | V-Lan: {self.vlan} | Switch: {self.switch}")


class SiteSwitchData(SwitchData):
    def __init__(self, data):
        super().__init__(data)
        self.switchPort = self.data[3]


hostname = "XXX"
load_dotenv()
ssh_user = os.getenv("USER")
ssh_pass = os.getenv("PASS")
c_switch_ip = os.getenv("CORE_SWITCH")
n_switch = os.getenv("NULL_SWITCH")

ip_address = socket.gethostbyname(hostname)
print(ip_address)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(c_switch_ip, username=ssh_user, password=ssh_pass)

command = f"sh ip arp | i {ip_address}"

print(command)
stdin, stdout, stderr = client.exec_command(command)
output = stdout.read().decode()
client.close()

CoreSwitchData = CoreSwitchData(output)

CoreSwitchData.show_data()

client2 = paramiko.SSHClient()
client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client2.connect(n_switch, username=ssh_user, password=ssh_pass)

command = f"sh mac address-table | i {CoreSwitchData.macaddress}"

stdin, stdout, stderr = client2.exec_command(command)
output2 = stdout.read().decode()
client2.close()

SiteSwitchData = SiteSwitchData(output2)

print(SiteSwitchData.switchPort)
