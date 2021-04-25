import socket


def repeat_scan(targets, ports):
    for ports in range(1, ports + 1):
        port_scan(targets, ports)


def port_scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(str(port) + ' open')
        sock.close()
    except:
        print(str(port) + ' Closed')


target = input("Add The Target IP: ")
ports = input('How Many Ports you want to scan?: ')

repeat_scan(target, int(ports))
