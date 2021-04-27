import platform  # For getting the operating system name
import os
import subprocess  # For executing a shell command
import time

from utils import MyMail


def check():
    current_os = platform.system().lower()
    parameter = '-n' if current_os == 'windows' else '-c'

    ip = "sv3.vn.boot.ai"
    ip = "192.168.1.57"
    exit_code = os.system(f"ping {parameter} 1 {ip}")
    print(exit_code)
    exit_code = os.popen(f"ping {parameter} 1 {ip}").read()
    if "unreachable" or "Request timed out" in exit_code:
        print(f"\n{ip} is down")
    else:
        print(f"\n{ip} is healthy")


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


if __name__ == '__main__':
    interval = 10  # time in seconds
    list_ip_addresses = ["sv2.vn.boot.ai", "sv3.vn.boot.ai", "13.212.239.89"]
    healthy_status = {}
    for ipaddress in list_ip_addresses:
        healthy_status[ipaddress] = True

    while True:
        for ipaddress in list_ip_addresses:
            if healthy_status[ipaddress] and ping(ipaddress) is False:
                healthy_status[ipaddress] = False
                my_mail = MyMail(ipaddress)
                my_mail.send_mail()
            elif not healthy_status[ipaddress] and ping(ipaddress) is True:
                healthy_status[ipaddress] = True
                my_mail = MyMail(ipaddress, server_status="UP")
                my_mail.send_mail()
        time.sleep(interval)
