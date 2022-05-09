import select
import socket
import sys
import queue

import tkinter
from tkinter import *

from jeu import *
from server import *
from clientA import *

# Config
HOST = "localhost"
BUFFER_SIZE = 2048               

class ClientB():     

    def connect(self):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

        # Reserve a port for your service
        PORT = 8044   

        # Bind to the port
        s.bind((HOST, PORT))            

        # Now wait for client connection
        s.listen(5)                     

        while True:
            # Establish connection with client
            conn, addr = s.accept()     
            print('Got connection from', addr)
            dataR = [self.listerouge]
            dataJ = [self.listejaune]
            conn.send(dataJ, dataR)
            conn.close()                