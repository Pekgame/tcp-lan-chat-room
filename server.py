print("Importing...")
import os
import threading
import socket
import pyperclip

os.system('cls')
hostname = socket. gethostname()
ip = socket. gethostbyname(hostname)

host = ip #"127.0.0.1"
port = int(input("Your custom Port(Can be 1-65535): "))
os.system('cls')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def copy(text):
    pyperclip.copy(text)

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print(f"Your IP: {ip}\nYour Port: {port}\nThe Port and IP is Copied to clipboard\nServer is listening...")
copy(f"IP: {ip}\nPort: {port}")
receive()
