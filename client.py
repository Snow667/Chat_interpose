import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

print(f"Connexion au server {HOST_IP}, port {HOST_PORT}...")
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("ERREUR: impossible de se connecter au server. Reconnexion...")
        time.sleep(4)
    else:
        print("Connecté au server")
        print("--------------")
        print()
        break

while True:
    message_server = s.recv(MAX_DATA_SIZE)
    if not message_server:
        break
    print("Message : ", message_server.decode())
    message_client = input("Vous : ")
    s.sendall(message_client.encode())



s.close()