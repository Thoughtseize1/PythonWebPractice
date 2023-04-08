import socket


def main():
    gost = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input("->")
    while message.lower().strip() != "exit":
        client_socket.send(message.encode())
        msg = client_socket.recv(1024).decode()
        print(f"Recived message: {msg}")

    client_socket.close()
