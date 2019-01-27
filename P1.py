from netmiko import ConnectHandler
from getpass import getpass


"""
device1 = {
    host="route-views.routeviews.org",
    username="rviews",
    password="rviews",
    device_type="cisco_ios",
#    session_log="my_session.txt", }

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
output =net_connect.send_command("show version",delay_factor=2,expect_string=r"Compiled")
print(output)
net_connect.disconnect()
"""


device = {
    "host": "route-views.routeviews.org",
    "username": "rviews",
#    "password": "rviews",
    "device_type": "cisco_nexus",
}

print("Enter Password for",device['host'])
device['password'] = getpass()
net_connect = ConnectHandler(**device)
output = net_connect.send_command("show version")

with open("output.txt", "w") as f:
  f.write(output)

print("hello")
