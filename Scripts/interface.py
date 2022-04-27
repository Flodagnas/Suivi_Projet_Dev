from ast import If
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

def accueil():
    global boutJouer,boutInscription,boutjouer,boutConnection,boutquitter,menujouer,menuInscription,menuAccueil,menuConnection
    destruction()
    dessin.itemconfigure( titre1 , text="Accueil")


    boutInscription = Button(fenetre,text='Inscription', width =11, command=inscription, font=ftComic,bg="black",fg="blue")
    boutInscription.grid (row =7,column = 3, padx = 10,pady = 10, columnspan =3)
    boutConnection = Button(fenetre,text='Connection', width =11, command=connection, font=ftComic,bg="black",fg="blue")
    boutConnection.grid (row =7,column =9, padx = 10,pady = 10, columnspan =3)
    boutJouer = Button(fenetre,text='Jouer', width =11, command=jouer, font=ftComic,bg="black",fg="blue")
    boutJouer.grid (row =12,column =6, padx =10,pady = 10, columnspan =3)

    menuAccueil=True
    menujouer=False
    menuInscription=False
    menuConnection=False

def inscription():
    global l1,l2, l3, e1, e2, rb1, rb2, b, menujouer,menuInscription,menuAccueil,menuConnection
    fenetrePrincipale = Tk()
    l1 = Label(fenetrePrincipale, text = "Pseudo").grid(row = 0, column = 0)
    e1 = Entry(fenetrePrincipale).grid(row = 0, column = 1)
    b = Button(fenetrePrincipale ,text="Submit", command = inscription).grid(row = 5, column = 1)
    if b == True:
        messagebox.showinfo("Statut de l'inscription", "Formulaire Envoyé")
        jouer()

    menuAccueil=False
    menujouer=True
    menuInscription=False
    menuConnection=False

def connection():
    pass

def jouer():
    global boutRejoindre, boutInvite, boutRetour,menujouer,menuInscription,menuAccueil,menuConnection
    destruction()
    dessin.itemconfigure( titre1 , text="Jouer")

    boutRejoindre = Button(fenetre,text='Rejoindre', width =11, command=rejoindre, font=ftComic,bg="black",fg="blue")
    boutRejoindre.grid (row =7,column = 3, padx = 10,pady = 10, columnspan =3)
    boutInvite = Button(fenetre,text='Invite', width =11, command=invite, font=ftComic,bg="black",fg="blue")
    boutInvite.grid (row =7,column =9, padx = 10,pady = 10, columnspan =3)

    boutRetour = Button(fenetre,text='Retour', width =11, command=jouer, font=ftComic,bg="black",fg="blue")
    boutRetour.grid (row =15,column =6, padx = 10,pady = 10, columnspan =3)

    menuAccueil=False
    menujouer=True
    menuInscription=False
    menuConnection=False

def rejoindre():
    pass

def invite():
    pass


def destruction():
    global boutJouer,boutInscription,boutcredit,boutjouer,boutleaderboard,boutConnection,boutquitter,menujouer,menuInscription,menuConnection
    if menuAccueil==True:
        boutConnection.destroy()
        boutInscription.destroy()
        boutJouer.destroy()

Xmax,Ymax=1500,1000
fenetre = Tk()
fenetre.title("Animation avec Tkinter")
dessin = Canvas(fenetre,bg='black',height=Ymax, width=Xmax)
dessin.grid (row = 1,column = 1, padx = 10,pady = 15, columnspan =13, rowspan =20)
fenetre.configure(bg='black')

ftComic = Font (family = 'Comic Sans MS', size = -25, underline = False, weight = "bold", slant="italic")
ftComic2 = Font (family = 'Comic Sans MS', size = 50, underline = True, weight = "bold", slant="italic")
ftComic3 = Font (family = 'Comic Sans MS', size = -20, underline = False, weight = "bold", slant="italic")

selfX1,selfY1=Xmax/2,40;100
titre1= dessin.create_text(selfX1,selfY1,text='Projet Matchmaking',fill='Blue', font= ftComic2)

boutjouer = Button(fenetre,text='Accueil', width =10, command=accueil, font=ftComic,bg="black",fg="blue")
boutjouer.grid (row = 10,column = 6, padx = 10,pady = 10, columnspan =3)
boutleaderboard = Button(fenetre,text='Inscription', width =11, command=inscription, font=ftComic,bg="black",fg="blue")
boutleaderboard.grid (row =13,column =6, padx = 10,pady =5, columnspan =3)
boutcredit = Button(fenetre,text='Connection', width =11, command=connection, font=ftComic,bg="black",fg="blue")
boutcredit.grid (row = 14,column = 6, padx = 10,pady = 5, columnspan =3)
boutquitter=Button(fenetre,text='Quitter', width =10, command=fenetre.destroy, font=ftComic,bg="black",fg="blue")
boutquitter.grid (row = 16,column = 6, padx = 10,pady = 10, columnspan =3)


fenetre.mainloop()