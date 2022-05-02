from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import sqlite3

def accueil():
    global boutJouer,boutInscription,boutConnection,boutquitter, Pseudo, mdp, Vérif_mdp, Submit, username, password, passentry, btn_login, userentry
    dessin.itemconfigure( titre1 , text="Accueil")

    boutInscription = Button(fenetre,text='Inscription', width =11, command=SignUp, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
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
    Pseudo.destroy()
    entry_pseudo.destroy()
    mdp.destroy()
    entry_mdp.destroy()
    Vérif_mdp.destroy()
    entry_Vérif.destroy()
    Submit.destroy()
    username.destroy()
    password.destroy()
    passentry.destroy()
    btn_login.destroy()
    userentry.destroy()

#-------------------------------------------------- Partie Inscription ----------------------------------------------------#

def SignUp():
    global entry_pseudo, entry_mdp, entry_Vérif, Submit, Pseudo, mdp, Vérif_mdp
    dessin.itemconfigure( titre1 , text="Inscription")
    Pseudo = Label(fenetre, text="Pseudo",width=20,font=("bold", 10))
    Pseudo.place(x=500,y=300)
    entry_pseudo = Entry(fenetre)
    entry_pseudo.place(x=700,y=300)
    mdp = Label(fenetre, text="Mot de Passe",width=20,font=("bold", 10))
    mdp.place(x=500,y=350)
    entry_mdp = Entry(fenetre)
    entry_mdp.place(x=700,y=350)
    Vérif_mdp = Label(fenetre, text="Vérification Mot de Passe",width=20,font=("bold", 10))
    Vérif_mdp.place(x=500,y=400)
    entry_Vérif = Entry(fenetre)
    entry_Vérif.place(x=700,y=400)
    Submit = Button(fenetre, text='Submit',width=20,bg='red',fg='white', command=executSignUp).place(x=600,y=450)

    boutJouer.destroy()
    boutInscription.destroy()
    boutConnection.destroy()
    boutquitter.destroy()

def executSignUp():
    global entry_pseudo, entry_mdp, entry_Vérif, Submit
    if entry_pseudo.get()=="" or entry_mdp.get()=="" or entry_Vérif.get()=="":
        messagebox.showerror("Error" , "All Fields Are Required" , parent = fenetre)
    if entry_mdp.get() != entry_Vérif.get():
        messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = fenetre)
    else:
        try:
            print("Je suis dans la fonction")
            con = sqlite3.connect('BDD.db')
            print("Connection réussie")
            cur = con.cursor()
            # cur.execute("select * from user where Pseudo=?",entry_pseudo.get())
            print("Select OK")
            row = cur.fetchone()
            print("Test 2")
            if row!=None:
                messagebox.showerror("Error" , "User Name Already Exits", parent = fenetre)
            else:
                print("test avant insert")
                cur.execute("insert into user(Pseudo,HashPassword) values(?,?)",(entry_pseudo.get(), entry_mdp.get()))
                print("test après insert")
                con.commit()
                con.close()
                messagebox.showinfo("Success" , "Registration Successfull" , parent = fenetre)
            
        except Exception as es:
            print("Erreur Exception")
            messagebox.showerror("Error" , f"Error : {str(es)}", parent = fenetre)

    accueil()

#-------------------------------------------------- Partie Connection ----------------------------------------------------#

def connection():
    global username, password, passentry, btn_login, userentry
    username = Label(fenetre, text= "User Name :" , font='Verdana 10 bold')
    username.place(x=60,y=220)
    password = Label(fenetre, text= "Password :" , font='Verdana 10 bold')
    password.place(x=60,y=260)
    userentry = Entry(fenetre, width=40 , textvariable = username)
    userentry.focus()
    userentry.place(x=200 , y=223)
    passentry = Entry(fenetre, width=40, show="*" ,textvariable = password)
    passentry.place(x=200 , y=260)

    # button login and clear
    btn_login = Button(fenetre, text = "Login" ,font='Verdana 10 bold',command = executLogin)
    btn_login.place(x=200, y=293)

    boutJouer.destroy()
    boutInscription.destroy()
    boutConnection.destroy()
    boutquitter.destroy()

def executLogin():
    global username, password, passentry, btn_login, userentry
    if userentry.get()=="" or passentry.get()=="":
        messagebox.showerror("Error","Enter User Name And Password",parent=fenetre)	
    else:
        try:
            con = sqlite3.connect('BDD.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM user WHERE Pseudo=? and HashPassword =?",(userentry.get(),passentry.get()))
            row = cur.fetchone()
            if row==None:
                messagebox.showerror("Error" , "Invalid User Name And Password", parent = fenetre)
            else:
                messagebox.showinfo("Success" , "Successfully Login" , parent = fenetre)
            con.close()
        except Exception as es:
            messagebox.showerror("Error" , f"Error : {str(es)}", parent = fenetre)
    accueil()

def jouer():
    global boutRejoindre, boutInvite, boutRetour
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
    boutOK.destroy()
    boutRetour2.destroy()

def rejoindre():
    global boutRejoindre, boutInvite, boutOK, boutRetour, boutRetour2
    dessin.itemconfigure( titre1 , text="Rejoindre")

    boutOK = Button(fenetre,text='Valider', width =11, command=jouer, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
    boutOK.grid (row =7,column =10, padx = 10,pady = 10, columnspan =3)
    boutRetour2 = Button(fenetre,text='Retour', width =11, command=jouer, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
    boutRetour2.grid (row =7,column =2, padx = 10,pady = 10, columnspan =3)

    boutRejoindre.destroy()
    boutInvite.destroy()
    boutRetour.destroy()

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

boutInscription = Button(fenetre,text='Inscription', width =11, command=SignUp, font=ftComic,bg="#D1D1D1",fg="#FF9E3D")
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
