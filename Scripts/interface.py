from tkinter import *
from tkinter.font import Font

def accueil():
    global boutarcade,boutsport,boutsalon,boutmystere,boutmenu,boutpartierapide,boutcredit,boutjouer,boutleaderboard,bouttournois,boutquitter,boutathletisme,boutbasket,boutmonopoly,boutshifumi,boutdame,boutretour,menujouer,menupartierapide,menuprincipal,menutournois
    destruction()
    dessin.itemconfigure( titre1 , text="Accueil")


    boutpartierapide = Button(fenetre,text='Partie Rapide', width =11, command=partierapide, font=ftComic,bg="black",fg="blue")
    boutpartierapide.grid (row =7,column = 3, padx = 10,pady = 10, columnspan =3)
    bouttournois = Button(fenetre,text='Tournois', width =11, command=tournois, font=ftComic,bg="black",fg="blue")
    bouttournois.grid (row =7,column =9, padx = 10,pady = 10, columnspan =3)
    boutmenu = Button(fenetre,text='Menu Principale', width =11, command=menuprincipale, font=ftComic,bg="black",fg="blue")
    boutmenu.grid (row =12,column =6, padx =10,pady = 10, columnspan =3)

    menuprincipal=False
    menujouer=True
    menupartierapide=False
    menutournois=False

def destruction():
    global boutarcade,boutsport,boutsalon,boutmystere,boutmenu,boutpartierapide,boutcredit,boutjouer,boutleaderboard,bouttournois,boutquitter,boutjeuarcade,boutathletisme,boutjeusport,boutbasket,boutmonopoly,boutshifumi,boutdame,boutretour,menujouer,menupartierapide,menuprincipal,menutournois
    if menuprincipal==True:
        boutjouer.destroy()
        boutleaderboard.destroy()
        boutcredit.destroy()
        boutquitter.destroy()
    if menujouer==True:
        bouttournois.destroy()
        boutpartierapide.destroy()
        boutmenu.destroy()
    if menupartierapide==True:
        boutathletisme.destroy()
        boutbasket.destroy()
        boutmonopoly.destroy()
        boutshifumi.destroy()
        boutdame.destroy()
        boutretour.destroy()
    if menutournois==True:
        boutarcade.destroy()
        boutsport.destroy()
        boutsalon.destroy()
        boutmystere.destroy()
        boutretour.destroy()

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