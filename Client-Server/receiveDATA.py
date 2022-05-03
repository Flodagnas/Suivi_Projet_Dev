import socket
from ..IHM import jeu

# Create a stream based socket(i.e, a TCP socket)
# operating on IPv4 addressing scheme
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Bind and listen
host = "10.44.18.2"
port = 9090
BUFFER_SIZE = 1024

serverSocket.bind((host, port));
serverSocket.listen();

# Accept connections
while(True):
    (clientConnected, clientAddress) = serverSocket.accept();
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));

    receiveData = clientConnected.recv(BUFFER_SIZE)
    print(receiveData.decode());

    # Send some data back to the client
    clientConnected.send("Hello Client!".encode());