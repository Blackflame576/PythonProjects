import socket
import threading
from datetime import*
# Connection Data
host = '127.0.0.104'
port = 6578

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print('[Server started!]')
# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(500000)
            broadcast(message)
        except:
            today=datetime.today()
            time=today.strftime('%X')
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{}:::{} вышел!'.format(time,nickname).encode('utf-8'))
            print('{}:::{} вышел!'.format(time,nickname))
            nicknames.remove(nickname)
            break
        
# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        today=datetime.today()
        time=today.strftime('%X')
        client, address = server.accept()
        print("{}:::{}присоединён!".format(time,str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(500000).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        client.send('Вы присоединены к серверу!'.encode('utf-8'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()