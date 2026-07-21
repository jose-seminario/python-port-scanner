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

print("*" * 42)
print("         Python Port Scanner")
print("*" * 42)

valid_port = False

ip = input("Enter IP address or domain: ")

while valid_port == False:
    try:
        port = int(input("Enter port: "))

    except:
        print("Please enter a valid number.")
        continue

    if 0 <= port <= 65535:
        valid_port = True
    else:
        print("Please enter a port between 0 and 65535.")

scanner(ip, port)