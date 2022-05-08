import tkinter
import random
from tkinter import *
from random import *
from tkinter import messagebox
from turtle import color

from ..SOCKETS.client_server import *

redscore   = 0  # Score de base à zéro
yelscore   = 0  # Score de base à zéro
running    = 1  # Définie si la partie est en cours ou arrêtée
manches    = 1  # Gestion des manches
casesJ     = []
casesR     = []

class Can(Canvas):

    global redscore, yelscore, running, manches

    def __init__(self):
        
        # Variables
        self.cases      = [] # Cases déjà remplies
        self.listerouge = [] # Liste des cases rouges
        self.listejaune = [] # Liste des cases jaunes
        self.dgagnantes = [] # Cases déjà gagnantes et donc ne peuvent plus l'être à nouveau
        self.couleur    = ["Rouges", "Jaunes"]
        self.color      = ["red", "yellow"]
        
        # Interface
        self.gclair     = "#BFBFBF"     # ligth gray
        self.gfonce     = "#8F8F8F"     # gray
        self.bclair     = "#5E5E5E"     # dark gray
        self.bfonce     = "#000"        # black    
        self.police1    = "Times 17 normal"
        self.police2    = "Arial 10 normal"
        self.police21   = "Arial 10 bold"
        self.police3    = "Times 15 bold"
        self.can        = Canvas.__init__(self, width =450, height = 600, bg=self.gfonce, bd=0)
        self.grid(row = 1, columnspan = 5)

        # On définit un joueur en aléatoire pour commencer la partie
        for _ in range(1):
            self.aleaJoueur = randint(0,1)
            print(self.aleaJoueur)

        # Joueur en cours
        self.joueur = self.aleaJoueur
        self.create_rectangle(20, 400, 120, 425, fill = self.gclair)
        self.create_text(35, 405, text ="Joueur :", anchor = NW, fill = self.bfonce, font= self.police21)

        # Continuer
        self.create_button = tkinter.Button(self.can, text = "Continuer", command = self.continuer)
        self.create_rectangle(330,400,405,425,fill=self.gclair)
        self.create_text(340, 405, text ="Continuer", anchor = NW, fill = self.bfonce, font= self.police2)
        
        if self.aleaJoueur == 0:
            self.indiccouleur = self.create_oval(95, 405, 110, 420, fill = self.color[0])
        elif self.aleaJoueur == 1:
            self.indiccouleur = self.create_oval(95, 405, 110, 420, fill = self.color[1])

        # Affichage des scores
        self.create_rectangle(20, 440, 350, 580, fill=self.gclair)
        self.create_text(35, 445, text= "AFFICHAGE DES SCORES", anchor = NW, fill= self.bfonce, font = self.police3)
        self.create_text(35, 475, text= "Manche : {0}".format(str(manches)), anchor = NW, fill= self.bfonce, font = self.police3)
        self.create_text(35, 510, text ="Rouges : {0}".format(str(redscore)), anchor = NW, fill = self.bfonce, font = self.police3)
        self.create_text(35, 535, text ="Jaunes : {0}".format(str(yelscore)), anchor = NW, fill = self.bfonce, font = self.police3)
        
        # Création des cases
        self.ovals = []
        for y in range(10, 390, 55):
            for x in range(10, 437, 63):
                self.ovals.append(self.create_oval(x, y, x + 50, y + 50 , fill= "white"))
                
        # En cas de click   
        self.bind("<Button-1>", self.click)
        
        # Pour relier à la fin les coordonnées des centres des cases
        self.coordscentres = []
        
        # Comptabilisation des suites de pièces
        self.rouges, self.jaunes = 0,0
        
        # Dictionnaire de reconnaissance
        self.dictionnaire = {}
        v = 0
        for y in range(10, 390, 55):
            for x in range(10, 437, 63):
                self.dictionnaire[(x, y, x + 50, y + 50)] = v
                v += 1
                self.coordscentres.append((x + 25, y + 25))

    def click(self,event): # En cas de click
        if 330 < event.x and 400 < event.y and event.x < 420 and event.y < 425:
            self.continuer()    # Nouvelle manche
            
        #Jeu en cours: reconnaissance de la case jouée    
        else :
            if running != 0:
                for (w, x, y, z) in self.dictionnaire:
                    if event.x > (w, x, y, z)[0] and event.y >(w, x, y, z)[1] and event.x < (w, x, y, z)[2] and event.y < (w, x, y, z)[3]:
                        self.colorier(self.dictionnaire[(w, x, y, z)])

                
    def colorier(self, n, nb=0): # Gère la coloration des cases
        
        if n in self.cases : return # Une case coloriée ne peut plus changer de couleur
           
        if n + 7 not in self.cases and n + 7 < 49: # Si la case en dessous est vide et existe, on essaie d'abord de colorier celle-là
            self.colorier(n+7)
            
        else:
            # Sinon on colorie celle-ci
            self.itemconfigure(self.ovals[n], fill = self.color[self.joueur])
            self.cases.append(n)
            self.color[self.joueur] == 'red' and self.listerouge.append(n) or self.listejaune.append(n)
            self.listejaune = [case for case in self.listejaune if case not in self.listerouge]
            self.verif(n)
            
            # Changement de joueur
            self.joueur = [0,1][[0,1].index(self.joueur)-1]
            self.itemconfigure(self.indiccouleur, fill = self.color[self.joueur])
    
    def verif(self, n): # Vérifie si la pièce ajoutée s'aligne avec trois autres déjà placées
        
        if running == 0 : return
        
        if n in self.listerouge and n+7  in self.listerouge and n+14  in self.listerouge and n+21 in self.listerouge: 
            liste = [n, n+7, n+14, n+21] 
            if self.gagnantes(liste) : self.win("rouges", liste[0], liste[3])
            return
        
        # idem pour jaunes
        if n in self.listejaune and n+7 in self.listejaune and n+14 in self.listejaune and n+21 in self.listejaune:
            liste = [n, n+7, n+14, n+21]
            if self.gagnantes(liste) : self.win("jaunes", liste[0], liste[3])
            return
        
        for x in (1,-6,8):
            
            if n in self.listerouge: # en s'assurant qu'elles ne sont trop près des bords (pour ne pas arriver de l'autre coté du plateau)
                if n % 7 != 6 and n+x in self.listerouge:
                    if n % 7 != 5 and n+ 2*x in self.listerouge:
                        if n % 7 != 4 and n + 3*x in self.listerouge:
                            liste = [n, n+x, n+2*x, n+3*x]
                            if self.gagnantes(liste) : self.win("rouges", liste[0], liste[3])
                            return
                        if n%7 > 0 and (n-x) in self.listerouge:
                            liste = [n-x,n, n+x, n+2*x]
                            if self.gagnantes(liste) : self.win("rouges", liste[0], liste[3])
                            return
                    if n%7 > 1 and (n-x) in self.listerouge:
                        if n%7 > 2 and n-(2*x) in self.listerouge:
                            liste = [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : self.win("rouges", liste[0], liste[3])
                            return
                        
            # Pareil pour les jaunes          
            if n in self.listejaune:
                if n % 7 != 6 and n+x in self.listejaune:
                    if n % 7 != 5 and n+ 2*x in self.listejaune:
                        if n % 7 != 4 and n + 3*x in self.listejaune:
                            liste = [n, n+x, n+2*x, n+3*x]
                            if self.gagnantes(liste) : self.win("jaunes", liste[0], liste[3])
                            return
                        if n%7 > 0 and (n-x) in self.listejaune:
                            liste = [n-x,n, n+x, n+2*x]
                            if self.gagnantes(liste) : self.win("jaunes", liste[0], liste[3])
                            return 
                    if n%7 > 1 and (n-x) in self.listejaune:
                        if n%7 > 2 and n-(2*x) in self.listejaune:
                            liste = [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : self.win("jaunes", liste[0], liste[3])
                            return
                        
        for x in (-1,6,-8):
            
            if n in self.listejaune:
                if n % 7 != 0 and (n+x) in self.listejaune:
                    if n % 7 != 1 and n+(2*x) in self.listejaune:
                        if n % 7 != 2 and n + (3*x) in self.listejaune:
                            liste = [n, n+x, n+2*x, n+3*x]
                            if self.gagnantes(liste) : self.win("jaunes", liste[0], liste[3])
                            return
                        if n%7 <6 and (n-x) in self.listejaune:
                            liste = [n-x,n, n+x, n+2*x]
                            if self.gagnantes(liste) : self.win("jaunes", liste[0], liste[3])
                            return
                    if n%7 < 5 and (n-x) in self.listejaune:
                        if n%7 < 4 and n-(2*x) in self.listejaune:
                            liste = [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : self.win("jaunes", liste[0], liste[3])
                            return
                        
            if n in self.listerouge:
                if n % 7 != 0 and (n+x) in self.listerouge:
                    if n % 7 != 1 and n+(2*x) in self.listerouge:
                        if n % 7 != 2 and n + (3*x) in self.listerouge:
                            liste = [n, n+x, n+2*x, n+3*x]
                            if self.gagnantes(liste) : self.win("rouges", liste[0], liste[3])
                            return
                        if n%7 <6 and (n-x) in self.listerouge:
                            liste = [n-x,n, n+x, n+2*x]
                            if self.gagnantes(liste) : self.win("rouges", liste[0], liste[3])
                            return
                    if n%7 < 5 and (n-x) in self.listerouge:
                        if n%7 < 4 and n-(2*x) in self.listerouge:
                            liste = [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : self.win("rouges", liste[0], liste[3])
                            return

    def continuer(self): # Pour passer à la manche suivante (victoire si l'un des joueurs est à 3 points)
        global running, redscore, yelscore, liste
        if ((self.cases ==49) or (running==0)) : # Empêche de passer à la manche suivante si le plateau n'est pas complet ou si un joueur n'a pas aligné 4 pionts
            self.update()

            if ((redscore == 3) or (yelscore == 3)):
                running = 0  
                self.verificationFinale()
            else: running = 1

            self.destroy()
            self.__init__()
        else :
            pass


    def verificationFinale(self): # Lorsque toutes les manches sont terminées
        global manches, redscore, yelscore

        # On comptabilise les points
        if redscore > yelscore :
            messagebox.showinfo("Partie terminée !", "Les Rouges ont gagnés !")
        
        elif yelscore < redscore :
            messagebox.showinfo("Partie terminée !", "Les Jaunes ont gagnés !")

    def win(self, qui, p, d, ): # Manche gagnée
        global running, redscore, yelscore, manches

        # Marquage des pièces gagnantes
        self.create_line (
            self.coordscentres[p][0], self.coordscentres[p][1],
            self.coordscentres[d][0], self.coordscentres[d][1],
            fill="blue",
            width=4
        )

        # Modification du score et de la manche
        if qui=="rouges" : 
            redscore += 1  
        if qui=="jaunes" : 
            yelscore += 1
        if (manches != 3):
            manches += 1

        running = 0        

    def gagnantes(self, liste=[]): # On vérifie que les pièces ne sont pas encore gagnantes, et on les ajoute dans la liste si elles le deviennent

        for i in liste:
            if i in self.dgagnantes: return 0
        
        for n in liste:
            self.dgagnantes.append(n)

        return 1

if __name__ ==	"__main__" :
    window = Tk()
    window.title("Jeu du Puissance 4")
    lecan = Can()
    window.mainloop()