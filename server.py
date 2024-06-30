import socket
import threading

clients = []

def broadcast_message(message, current_client):
    for client in clients:
        if client != current_client:
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received: {message}")
                broadcast_message(message, client_socket)
            else:
                break
        except:
            break

    client_socket.close()
    clients.remove(client_socket)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(2)
    print("Server started on port 5555")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
