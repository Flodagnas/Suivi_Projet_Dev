import tkinter
from tkinter import *

root = tkinter.Tk() # Création de la fenêtre racine
root.geometry("1200x700")

btnJouer = tkinter.Button (
  root,
  text = "LEFT",
  activeforeground = "white",
  activebackground = "grey",
  padx = 8,
  pady = 5
)


btnJouer.pack()
root.mainloop() # Lancement de la boucle principale