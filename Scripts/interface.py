from tkinter import *
from tkinter.font import Font
import connexion
import inscription

def accueil():
    global boutJouer,boutInscription,boutConnection,boutquitter,menujouer,menuInscription,menuAccueil,menuConnection, menuInviter, menuRejoindre
    dessin.itemconfigure( titre1 , text="Accueil")

    boutInscription = Button(fenetre,text='Inscription', width =11, command=inscription, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
    boutInscription.grid (row =12,column =6, padx = 10,pady =5, columnspan =3)
    boutConnection = Button(fenetre,text='Connection', width =11, command=connection, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
    boutConnection.grid (row = 13,column = 6, padx = 10,pady = 5, columnspan =3)
    boutJouer = Button(fenetre,text='Jouer', width =11, command=jouer, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
    boutJouer.grid (row = 14,column = 6, padx = 10,pady = 5, columnspan =3)
    boutquitter=Button(fenetre,text='Quitter', width =10, command=fenetre.destroy, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
    boutquitter.grid (row = 15,column = 6, padx = 10,pady = 10, columnspan =3)

    boutRejoindre.destroy()
    boutInvite.destroy()
    boutRetour.destroy()

    menuAccueil=True
    menujouer=False
    menuInscription=False
    menuConnection=False
    menuRejoindre=False
    menuInviter=False


def inscription():
    signup

def connection():
    login

def jouer():
    global boutRejoindre, boutInvite, boutRetour, menujouer, menuInscription, menuAccueil, menuConnection, menuRejoindre, menuInviter
    dessin.itemconfigure( titre1 , text="Jouer")

    boutRejoindre = Button(fenetre,text='Rejoindre', width =11, command=rejoindre, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
    boutRejoindre.grid (row =7,column = 3, padx = 10,pady = 10, columnspan =3)
    boutInvite = Button(fenetre,text='Invite', width =11, command=invite, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
    boutInvite.grid (row =7,column =9, padx = 10,pady = 10, columnspan =3)
    boutRetour = Button(fenetre,text='Retour', width =11, command=accueil, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
    boutRetour.grid (row =15,column =6, padx = 10,pady = 10, columnspan =3)

    boutJouer.destroy()
    boutInscription.destroy()
    boutConnection.destroy()
    boutquitter.destroy()

    menuAccueil=False
    menujouer=True
    menuInscription=False
    menuConnection=False
    menuRejoindre=False
    menuInviter=False

def rejoindre():
    pass

def invite():
    pass



fenetre = Tk()
Xmax,Ymax=fenetre.winfo_screenwidth()-50, fenetre.winfo_screenheight()-100
fenetre.title("Suivi Projet Dev")
dessin = Canvas(fenetre,bg='#AFADAD',height=Ymax, width=Xmax)
dessin.grid (row = 1,column = 1, padx = 10,pady = 15, columnspan =13, rowspan =20)

#Texte Basique#
ftComic = Font (family = 'Comic Sans MS', size = -25, underline = False, weight = "bold", slant="italic")

#Titre#
ftComic2 = Font (family = 'Comic Sans MS', size = 50, underline = True, weight = "bold", slant="italic")

ftComic3 = Font (family = 'Comic Sans MS', size = -20, underline = False, weight = "bold", slant="italic")

selfX1,selfY1=Xmax/2,40;100
titre1= dessin.create_text(selfX1,selfY1,text='Projet Matchmaking',fill='Red', font= ftComic2)

boutInscription = Button(fenetre,text='Inscription', width =11, command=inscription, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
boutInscription.grid (row =12,column =6, padx = 10,pady =5, columnspan =3)
boutConnection = Button(fenetre,text='Connection', width =11, command=connection, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
boutConnection.grid (row = 13,column = 6, padx = 10,pady = 5, columnspan =3)
boutJouer = Button(fenetre,text='Jouer', width =11, command=jouer, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
boutJouer.grid (row = 14,column = 6, padx = 10,pady = 5, columnspan =3)
boutquitter=Button(fenetre,text='Quitter', width =10, command=fenetre.destroy, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
boutquitter.grid (row = 15,column = 6, padx = 10,pady = 10, columnspan =3)

menuAccueil=True
menujouer=False
menuInscription=False
menuConnection=False
menuRejoindre=False
menuInviter=False

fenetre.mainloop()
