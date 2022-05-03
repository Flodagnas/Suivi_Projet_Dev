import tkinter
import random
from tkinter import *
from random import *

class Can(Canvas):

    def __init__(self):
        
        # Variables
        self.cases      = [] # Cases déjà remplies
        self.listerouge = [] # Liste des cases rouges
        self.listejaune = [] # Liste des cases jaunes
        self.dgagnantes = [] # Cases déjà gagnantes et donc ne peuvent plus l'être à nouveau
        self.running    = 1  # Partie en cours
        self.manche     = 1 # Compte le nombre de manche (partie gagnée au bout de 3 manches gagnées)

        # on compte les victoires pour chaque manche, pour pouvoir savoir qui gagne la partie
        self.winjaune = 0 # Joueur jaune qui vient de gagner la manche 
        self.winrouge = 0 # Joueur rouge qui vient de gagner la manche

        self.couleur    = ["Rouges", "Jaunes"]
        self.color      = ["red", "yellow"]
        
        # Interface
        self.clair      = "light gray"
        self.fonce      = "gray"
        self.police1    = "Times 17 normal"
        self.police2    = "Arial 10 normal"
        self.can        = Canvas.__init__(self, width =1200, height = 700, bg=self.fonce, bd=0)
        self.grid(row = 1, columnspan = 5)
        
        # On définit un joueur en aléatoire pour commencer la partie
        for _ in range(1):
            self.aleaJoueur = randint(0,1)
            print(self.aleaJoueur)

        # Joueur en cours
        self.joueur = self.aleaJoueur
        self.create_rectangle(20, 400, 115, 425, fill = self.clair)
        self.create_text(35, 405, text ="Joueur :", anchor = NW, fill = self.fonce, font= self.police2)
        
        if self.aleaJoueur == 0:
            self.indiccouleur = self.create_oval(85, 405, 100, 420, fill = self.color[0])
        elif self.aleaJoueur == 1:
            self.indiccouleur = self.create_oval(85, 405, 100, 420, fill = self.color[1])
    
        # Bouton Nouveau Jeu
        self.create_rectangle(330, 400, 420, 425, fill=self.clair)
        self.create_text(340, 405, text ="Nouveau jeu", anchor = NW, fill = self.fonce, font= self.police2)
        
        # Création des cases
        self.ovals = []
        for y in range(10, 390, 55):
            for x in range(10, 437, 63):
                self.ovals.append(self.create_oval(x, y, x + 50, y + 50 , fill= "white"))
                
        # En cas de clic  
        self.bind("<Button-1>", self.clic)
        
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

    def clic(self, event): # En cas de clic
        if 330 < event.x and 400 < event.y and event.x < 420 and event.y < 425:
            self.new()# => Nouveau jeu
            # Jeu en cours: reconnaissance de la case jouée
            
        else :
            if self.running != 0:
                for (w, x, y, z) in self.dictionnaire:
                    if event.x > (w, x, y, z)[0] and event.y >(w, x, y, z)[1] and event.x < (w, x, y, z)[2] and event.y < (w, x, y, z)[3]:
                        self.colorier(self.dictionnaire[(w, x, y, z)]) # => Jouer

                
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

            # On regarde toutes les cases sont remplies
            self.verificationFinale()
    
    def verif(self, n): # Vérifie si la pièce ajoutée s'aligne avec trois autres déjà placées
        
        if self.running == 0 : return
        
        if n in self.listerouge and n+7 in self.listerouge: 
            # D'abbord à la verticale,
            # séparément car proximité d'un bord inintéressante
            liste=[n]
            if self.gagnantes(liste) : self.win("rouges", liste[0],liste[3])
            return
        
        # idem pour jaunes
        if n in self.listejaune and n+7 in self.listejaune:
            liste=[n]
            if self.gagnantes(liste) : self.win("jaunes", liste[0],liste[3])
            return
        
        for x in (1,-6,8):
            
            if n in self.listerouge: # en s'assurant qu'elles ne sont trop près des bords (pour ne pas arriver de l'autre coté du plateau)
                if n % 7 != 6 and n+x in self.listerouge:
                    if n % 7 != 5 and n+ 2*x in self.listerouge:
                        if n % 7 != 4 and n + 3*x in self.listerouge:
                            liste = [n, n+x, n+2*x, n+3*x]
                            if self.gagnantes(liste) : self.win("rouges", liste[0],liste[3])
                            return
                        if n % 7 > 0 and (n-x) in self.listerouge:
                            liste = [n-x,n, n+x, n+2*x]
                            if self.gagnantes(liste) : self.win("rouges", liste[0],liste[3])
                            return
                    if n%7 > 1 and (n-x) in self.listerouge:
                        if n % 7 > 2 and n-(2*x) in self.listerouge:
                            liste = [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : self.win("rouges", liste[0],liste[3])
                            return
                        
            # Pareil pour les jaunes     
            if n in self.listejaune:
                if n % 7 != 6 and n+x in self.listejaune:
                    if n % 7 != 5 and n+ 2*x in self.listejaune:
                        if n % 7 != 4 and n + 3*x in self.listejaune:
                            liste = [n, n+x, n+2*x, n+3*x]
                            if self.gagnantes(liste) : self.win("jaunes", liste[0],liste[3])
                            return
                        if n % 7 > 0 and (n-x) in self.listejaune:
                            liste = [n-x,n, n+x, n+2*x]
                            if self.gagnantes(liste) : self.win("jaunes", liste[0],liste[3])
                            return
                    if n%7 > 1 and (n-x) in self.listejaune:
                        if n % 7 > 2 and n-(2*x) in self.listejaune:
                            liste = [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : self.win("jaunes", liste[0],liste[3])
                            return
                              
        for x in (-1,6,-8):
            
            if n in self.listejaune:
                if n % 7 != 0 and (n+x) in self.listejaune:
                    if n % 7 != 1 and n+(2*x) in self.listejaune:
                        if n % 7 != 2 and n + (3*x) in self.listejaune:
                            liste = [n, n+x, n+2*x, n+3*x]
                            if self.gagnantes(liste) : self.win("jaunes", liste[0],liste[3])
                            return
                        if n%7 <6 and (n-x) in self.listejaune:
                            liste = [n-x,n, n+x, n+2*x]
                            if self.gagnantes(liste) : self.win("jaunes", liste[0],liste[3])
                            return
                    if n%7 < 5 and (n-x) in self.listejaune:
                        if n%7 < 4 and n-(2*x) in self.listejaune:
                            liste = [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : self.win("jaunes", liste[0],liste[3])
                            return
                        
            if n in self.listerouge:
                if n % 7 != 0 and (n+x) in self.listerouge:
                    if n % 7 != 1 and n+(2*x) in self.listerouge:
                        if n % 7 != 2 and n + (3*x) in self.listerouge:
                            liste = [n, n+x, n+2*x, n+3*x]
                            if self.gagnantes(liste) : self.win("rouges", liste[0],liste[3])
                            return
                        if n%7 <6 and (n-x) in self.listerouge:
                            liste = [n-x,n, n+x, n+2*x]
                            if self.gagnantes(liste) : self.win("rouges", liste[0],liste[3])
                            return
                    if n%7 < 5 and (n-x) in self.listerouge:
                        if n%7 < 4 and n-(2*x) in self.listerouge:
                            liste = [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : self.win("rouges", liste[0],liste[3])
                            return

    def verificationFinale(self): # Cumule des points pour les manches
        
        if len(self.manche)==3: # On vérifie que l'on est à la manche 3
            typ = self.verifpartie() # Type de partie gagnée

            if typ[1]==0:
                self.texte2 = Label(window, text = "Les " + typ[0] + " ont définitivement gagnés !", bg= self.fonce,
                                    fg=self.clair, font=self.police1)
                
            elif typ[1]==1:
                self.texte2 = Label(window, text = "Les " + typ[0] + " ont gagnés la première manche !", bg= self.fonce,
                                    fg=self.clair, font=self.police1)
                
            else:
                self.texte2 = Label(window, text = typ[0], bg= self.fonce, fg=self.clair, font=self.police1)

                
    def win(self, qui, p, d): # Partie gagnée
        
        # Marquage des pièces gagnantes
        self.create_line (
            self.coordscentres[p][0], self.coordscentres[p][1],
            self.coordscentres[d][0], self.coordscentres[d][1],
            fill="blue", 
            width=4
        )

        if qui=="rouges" : self.rouges += 1 # Comptabilisation des suites
        if qui=="jaunes" : self.jaunes += 1

        if self.running == 3:
            self.pRouges.config(text = "Rouges : " + str(self.rouges))
            self.pJaunes.config(text = "Jaunes : " + str(self.jaunes))
            return

        # Affichage des scores
        self.qui = qui
        self.texte = Label(window, text="Les %s ont gagnés cette manche!" % (qui), bg= self.fonce, fg=self.clair, font=self.police1)
         
        if self.qui == "rouges" : self.winrouge += 1
        if self.qui == "jaunes" : self.winjaune += 1
        self.texte.grid()
        self.running = 0
        self.manche += 1

        
    def gagnantes(self, liste=[]): # On vérifie que les pièces ne sont pas encore gagnantes, et on les ajoute dans la liste si elles le deviennent

        for i in liste:
            if i in self.dgagnantes: return 0
        
        for n in liste:
            self.dgagnantes.append(n)
            
        return 1

    
    def verifpartie(self): # Donner le résultat final
        if self.manche == 3 :
            if self.rouges > self.jaunes    : return "Rouges",0
            if self.jaunes > self.rouges    : return "Jaunes",0
            if self.rouges != 0             : return self.qui, 1 # En cas d'égalité, le premier à avoir aligné ses pièces gagne

        return "Personne n'a gagné", 2 # Sinon, tous deux ont perdu

    def new(self):# Nouveau Jeu
        try:
            self.texte.destroy()
        except:
            pass
        try:
            self.texte2.destroy()
        except:
            pass
        try:
            self.pRouges.destroy()
        except:	
            pass
        try:
            self.pJaunes.destroy()
        except:
            pass
    
        self.destroy()
        self.__init__()

	
if __name__ ==	"__main__" :
    window = Tk()
    window.title("Puissance 4 : Matchmaking")
    window.config(bg="gray")
    lecan = Can()
    window.mainloop()