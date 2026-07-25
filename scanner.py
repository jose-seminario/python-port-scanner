import socket
from ui import show_progress


def scanner(ip, port):
    connection = socket.socket()
    connection.settimeout(1)

    try:
        connection.connect((ip, port))
        return True

    except:
        return False

    finally:
        connection.close()


def get_service(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown"


def scan_port_range(ip, start_port, end_port):
    open_ports = []

    total_ports = end_port - start_port + 1

    for port in range(start_port, end_port + 1):

        scanned_ports = port - start_port + 1
        progress = (scanned_ports / total_ports) * 100
        show_progress(progress)

        if scanner(ip, port):
            service = get_service(port)
            open_ports.append((port, service))

    print()
    return open_ports