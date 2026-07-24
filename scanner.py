import socket


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

    for port in range(start_port, end_port + 1):
        if scanner(ip, port):
            service = get_service(port)
            open_ports.append((port, service))
    return open_ports

    