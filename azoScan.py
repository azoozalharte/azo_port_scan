import socket


def repeat_scan(target, ports):
    print('\n' + 'Starting Scan For ' + str(target))
    for port in range(1, ports + 1):
        port_scan(target, port)


def port_scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Open: " + str(port))
        sock.close()
    except:
        pass


targets = input("[*] Enter Targets To Scan(split them by , If there any): ")
ports = input(
    '[*] Enter How Many Ports You Want 19To Scan: ')

if ',' in targets:
    print('[*] Scaning Multiple Targets')
    for ip_addr in targets.split(','):
        repeat_scan(ip_addr.strip(' '), int(ports))
else:
    repeat_scan(targets, int(ports))
