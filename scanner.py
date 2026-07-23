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


def scan_port_range(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        if scanner(ip, port):
            print(f"[OPEN] Port {port}")
