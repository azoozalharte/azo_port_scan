import socket
import os
import platform


def check_ping(target):
    response = os.system(
        "ping " + ("-n 1 " if platform.system().lower() == "windows" else "-c 1 ") + target)
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = 'Network Error'
    return pingstatus


def repeat_scan(target, ports):
    print('\n' + 'Target: ' + str(target))
    for port in range(1, ports + 1):
        port_scan(target, port)


def port_scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Open: " + str(port) + ' ' +
              socket.getservbyport(port, 'tcp'))
        sock.close()
    except:
        pass


targets = input("[*] Enter Targets To Scan(split them by , If there any): ")
ports = input('[*] Enter How Many Ports You Want To Scan: ')

if ',' in targets:
    print('[*] Scaning Multiple Targets')

    for ip_addr in targets.split(','):
        if check_ping(ip_addr.strip(' ')) == "Network Active":
            repeat_scan(ip_addr.strip(' '), int(ports))
        else:
            print('\n' +
                  "[-] This Target is offline or out of your network: " + ip_addr.strip(' '))
            pass
elif check_ping(targets) == "Network Active":
    print('[*] Scaning Single Target')
    repeat_scan(targets, int(ports))
else:
    print('\n' +
          "[-] This Target is offline or out of your network: " + targets)
