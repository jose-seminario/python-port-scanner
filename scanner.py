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
    for port in range(start_port, end_port + 1):
        if scanner(ip, port):
            service = get_service(port)
            print(f"[OPEN] Port {port} - {service}")
            