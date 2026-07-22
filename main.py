import socket


def scanner(ip, port):
    print(f"Scanning port {port}...")

    connection = socket.socket()

    try:
        connection.connect((ip, port))
        print("Port is open")

    except:
        print("Port is closed")

    finally:
        connection.close()


def show_banner():
    print("*" * 42)
    print("         Python Port Scanner")
    print("*" * 42)


def show_menu():
    print("1. Scan a specific port or a port range")
    print("2. Scan all ports")


def get_user_option():
    valid_option = False

    while not valid_option:
        try:
            user_option = int(input("Choose an option: "))

        except:
            print("Please enter a valid number.")
            continue

        if user_option == 1 or user_option == 2:
            valid_option = True
        else:
            print("Please choose option 1 or 2.")

    return user_option


def get_ip():
    ip = input("Enter IP address or domain: ")
    return ip


def get_port():
    valid_port = False

    while not valid_port:
        try:
            port = int(input("Enter port: "))

        except:
            print("Please enter a valid number.")
            continue

        if 0 <= port <= 65535:
            valid_port = True
        else:
            print("Please enter a port between 0 and 65535.")

    return port


show_banner()
show_menu()

option = get_user_option()

ip = get_ip()
port = get_port()

scanner(ip, port)
