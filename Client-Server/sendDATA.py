import socket
from ..IHM import jeu

# Create a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Connect to the server
host = "10.44.18.2"
port = 9090
BUFFER_SIZE = 1024

clientSocket.connect((host, port));

# Send data to server
data = "Hello Server!";
clientSocket.send(data.encode());

# Receive data from server
receiveData = clientSocket.recv(BUFFER_SIZE);

# Print to the console
print(receiveData.decode());