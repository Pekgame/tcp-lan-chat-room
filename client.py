print("Importing...")
import os
import socket
import threading

os.system('cls')
while True:
    host_ip = input("Your Host IP: ")
    os.system('cls')
    host_port = int(input("Your Host Port: "))
    os.system('cls')

    def run():
        nickname = input("Choose a nick name: ")
        os.system('cls')

        def receive():
            while True:
                try:
                    message = client.recv(1024).decode('ascii')
                    if message == 'NICK':
                        client.send(nickname.encode('ascii'))
                    else:
                        print(message)
                except:
                    print("An error occurred!")
                    client.close()
                    break

        def write():
            while True:
                message = f'{nickname}: {input("")}'
                client.send(message.encode('ascii'))

        receive_thread = threading.Thread(target=receive)
        receive_thread.start()

        write_thread = threading.Thread(target=write)
        write_thread.start()

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host_ip, host_port))
        run()
        break
    except:
        print("Error!\nUncorrect Port os IP!")
        continue
