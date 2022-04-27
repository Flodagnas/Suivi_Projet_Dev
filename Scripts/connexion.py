from tkinter import *
from tkinter import messagebox
import sqlite3


#---------------------------------------------------------------Login Function --------------------------------------
def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)

def close():
	win.destroy()	


def login():
	if username.get()=="" or password.get()=="":
		messagebox.showerror("Error","Enter User Name And Password",parent=win)	
	else:
		try:
			con = sqlite3.connect('BDD.db')
			cur = con.cursor()
            
			cur.execute("SELECT * FROM user WHERE Pseudo=? and HashPassword =?",(username.get(),password.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

			else:
				messagebox.showinfo("Success" , "Successfully Login" , parent = win)
				close()
			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error : {str(es)}", parent = win)

#---------------------------------------------------------------End Login Function ---------------------------------

win = Tk()

# app title
win.title("App")

# window size
win.maxsize(width=500 ,  height=500)
win.minsize(width=500 ,  height=500)


#heading label
heading = Label(win , text = "Login" , font = 'Verdana 25 bold')
heading.place(x=60 , y=150)

username = Label(win, text= "User Name :" , font='Verdana 10 bold')
username.place(x=60,y=220)

userpass = Label(win, text= "Password :" , font='Verdana 10 bold')
userpass.place(x=60,y=260)

# Entry Box
username = StringVar()
password = StringVar()
	
userentry = Entry(win, width=40 , textvariable = username)
userentry.focus()
userentry.place(x=200 , y=223)

passentry = Entry(win, width=40, show="*" ,textvariable = password)
passentry.place(x=200 , y=260)


# button login and clear

btn_login = Button(win, text = "Login" ,font='Verdana 10 bold',command = login)
btn_login.place(x=200, y=293)


btn_login = Button(win, text = "Clear" ,font='Verdana 10 bold', command = clear)
btn_login.place(x=260, y=293)


win.mainloop()
#-------------------------------------------------------------------------- End Login Window ---------------------------------------------------