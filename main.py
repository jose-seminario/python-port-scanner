import socket

print("*" * 42)
print("         Python Port Scanner")
print("*" * 42)

ip = input("Enter IP: ")
puerto = input("Enter Port: ")

scanner = socket.socket()

try:
    scanner.connect((ip, int(puerto)))
    print("CONNECTED")
except:
    print("CLOSED")