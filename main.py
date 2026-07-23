import socket


def scanner(ip, port):
    connection = socket.socket()

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


def show_banner():
    print("*" * 42)
    print("         Python Port Scanner")
    print("*" * 42)


def show_menu():
    print("1. Scan a specific port or a port range")
    print("2. Scan all ports")


def get_user_option():
    while True:
        try:
            user_option = int(input("Choose an option: "))

        except:
            print("Please enter a valid number.")
            continue

        if user_option == 1 or user_option == 2:
            return user_option

        print("Please choose option 1 or 2.")


def get_ip():
    return input("Enter IP address or domain: ")


def get_port_range():
    while True:
        try:
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))

        except:
            print("Please enter a valid number.")
            continue

        if not (0 <= start_port <= 65535):
            print("Start port must be between 0 and 65535.")
            continue

        if not (0 <= end_port <= 65535):
            print("End port must be between 0 and 65535.")
            continue

        if start_port > end_port:
            print("Start port cannot be greater than end port.")
            continue

        return start_port, end_port


show_banner()
show_menu()

option = get_user_option()

if option == 1:
    ip = get_ip()
    start_port, end_port = get_port_range()
    scan_port_range(ip, start_port, end_port)

elif option == 2:
    ip = get_ip()
    scan_port_range(ip, 1, 65535)