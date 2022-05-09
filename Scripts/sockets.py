import select
import socket
import sys
import queue

import tkinter
from tkinter import *

from jeu import *

# Config
HOST = "localhost"
BUFFER_SIZE = 2048


class Server():

    # Créer un socket TCP / IP
    server = socket.socket()
    server.setblocking(0)
    # Liez le socket au port
    server.bind((HOST, PORT))
    # Écoutez les connexions entrantes
    server.listen(5)
    # Sockets à partir desquels nous nous attendons à lire
    inputs = [server]
    # Sockets dans lesquels nous nous attendons à écrire
    outputs = []
    # Files d'attente de messages sortants
    msg = {}
    while inputs:
        # Attendez qu'au moins une des sockets soit prête pour le traitement
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # Gérer les entrées
        for s in readable:
            if s is server:
                # Un socket serveur "readable" est prêt à accepter une connexion
                connection, client_address = s.accept()
                connection.setblocking(0)
                inputs.append(connection)
                # Donner à la connexion une file d'attente pour les données que nous voulons envoyer
                msg[connection] = queue.Queue()
            else:
                data = s.recv(BUFFER_SIZE)
                # Un socket client "readable" contient des données
                if data:
                    msg[s].put(data)
                    if s not in outputs:
                        outputs.append(s)
                else:
                    # Interpréter le résultat vide comme une connexion fermée
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()
                    del msg[s]
        # Gérer les sorties
        for s in writable:
            try:
                next_msg = msg[s].get_nowait()
            except queue.Empty:
                # Aucun message en attente, alors arrêtez de vérifier l'écriture.
                outputs.remove(s)
            else:
                s.send(next_msg)
        #Gérer les exceptions
        for s in exceptional:
            # Arrêtez d'écouter les entrées sur la connexion
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            del msg[s]

class ClientA():

    def connect(self):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

        # Reserve a port for your service
        PORT = 8004   

        # Bind to the port
        s.bind((HOST, PORT))            

        # Now wait for client connection
        s.listen(5)                     

        while True:
            # Establish connection with client
            conn, addr = s.accept()     
            print('Got connection from', addr)
            data = [self.listerouge]
            conn.send('Thank you for connecting')
            conn.close()                

class ClientB():                         

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
        conn.send('Thank you for connecting')
        conn.close()                