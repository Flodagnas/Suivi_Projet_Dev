from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
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
            
			cur.execute("SELECT * FROM user WHERE username=%s and password = %s",(username.get(),password.get()))
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

#----------------------------------------------------------- Signup Window --------------------------------------------------

def signup():
	# signup database connect 
	def action():
		if username.get()=="" or password.get()=="" or verif_pass.get()=="":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
		elif password.get() != verif_pass.get():
			messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
		else:
			try:
				con = sqlite3.connect('BDD.db')
				cur = con.cursor()
				cur.execute("select * from user where username=%s",username.get())
				row = cur.fetchone()
				if row!=None:
					messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
				else:
					cur.execute("insert into user(username,password) values(%s,%s)",
                    (
                        username.get(),
                        password.get()
                    ))
					con.commit()
					con.close()
					messagebox.showinfo("Success" , "Ragistration Successfull" , parent = winsignup)
					clear()
					switch()
				
			except Exception as es:
				messagebox.showerror("Error" , f"Error : {str(es)}", parent = winsignup)

	# close signup function			
	def switch():
		winsignup.destroy()

	# clear data function
	def clear():
		username.delete(0,END)
		password.delete(0,END)
		verif_pass.delete(0,END)


	# start Signup Window	

	winsignup = Tk()
	winsignup.title("App")
	winsignup.maxsize(width=500 ,  height=500)
	winsignup.minsize(width=500 ,  height=500)


	#heading label
	heading = Label(winsignup , text = "Signup" , font = 'Verdana 20 bold')
	heading.place(x=60 , y=150)

	username = Label(winsignup, text= "User Name :" , font='Verdana 10 bold')
	username.place(x=60,y=220)

	password = Label(winsignup, text= "Password :" , font='Verdana 10 bold')
	password.place(x=60,y=260)

	verif_pass = Label(winsignup, text= "Verify Password:" , font='Verdana 10 bold')
	verif_pass.place(x=60,y=300)

	# Entry Box ------------------------------------------------------------------

	username = StringVar()
	password = StringVar()
	verif_pass = StringVar()


	username = Entry(winsignup, width=40,textvariable = username)
	username.place(x=200 , y=223)

	
	password = Entry(winsignup, width=40, show="*", textvariable = password)
	password.place(x=200 , y=260)

	
	verif_pass= Entry(winsignup, width=40 ,show="*" , textvariable = verif_pass)
	verif_pass.place(x=200 , y=300)


	# button login and clear

	btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action)
	btn_signup.place(x=200, y=413)


	btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
	btn_login.place(x=280, y=413)


	sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
	sign_up_btn.place(x=350 , y =20)


	winsignup.mainloop()
#---------------------------------------------------------------------------End Singup Window-----------------------------------	

#------------------------------------------------------------ Login Window -----------------------------------------

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

# signup button

sign_up_btn = Button(win , text="Switch To Sign up" , command = signup )
sign_up_btn.place(x=350 , y =20)


win.mainloop()
#-------------------------------------------------------------------------- End Login Window ---------------------------------------------------