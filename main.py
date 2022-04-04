import platform
import subprocess
import time

from enums import IP_ADDRESSES, INTERVAL
from utils import MyMail


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
    """
    python main.py
    """
    healthy_status = {}
    for ipaddress in IP_ADDRESSES:
        healthy_status[ipaddress] = True

    while True:
        for ipaddress in IP_ADDRESSES:
            if healthy_status[ipaddress] and ping(ipaddress) is False:
                healthy_status[ipaddress] = False
                my_mail = MyMail(ipaddress)
                my_mail.send_mail()
            elif not healthy_status[ipaddress] and ping(ipaddress) is True:
                healthy_status[ipaddress] = True
                my_mail = MyMail(ipaddress, server_status="UP")
                my_mail.send_mail()
        time.sleep(INTERVAL)
