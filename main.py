import socket

def scanner(ip, port):
    print(f"Escaneando el puerto {port}...")

    conexion = socket.socket()

    try:
        conexion.connect((ip, port))
        print("Puerto abierto")

    except:
        print("Puerto cerrado")

    finally:
        conexion.close()

print("*" * 42)
print("         Python Port Scanner")
print("*" * 42)

puerto_valido = False

ip = input("Ingrese la IP o dominio: ")

while puerto_valido == False:
    try:
        puerto = input("Enter Port: ")
        puerto = int(puerto)

    except:
        print("Inserte un número válido")
        continue

    if puerto >= 0 and puerto <= 65535:
        puerto_valido = True
    else:
        print("Ingrese un puerto entre 0 y 65535")

scanner(ip, puerto)
