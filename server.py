import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Pour erreur "already used"
s.bind((HOST_IP, HOST_PORT)) # entre 10000 et 65000
s.listen()

print(f"Attente de connexion {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_adress = s.accept()
print("Connexion établie avec", client_adress)
print("--------------")
print()

while True:
    message_server = input("Vous : ")
    connection_socket.sendall(message_server.encode())
    message_client = connection_socket.recv(MAX_DATA_SIZE)
    if not message_client:
        break
    print("Message :", message_client.decode())


s.close()
connection_socket.close()