from tkinter import *
from tkinter import messagebox
import sqlite3

class signup:
    def clear():
        userentry.delete(0,END)
        passentry.delete(0,END)

    def close():
        winsignup.destroy()	

    #----------------------------------------------------------- Signup Window --------------------------------------------------
    def action():
        if username.get()=="" or password.get()=="" or verif_pass.get()=="":
            messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
        elif password.get() != verif_pass.get():
            messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
        else:
            try:
                con = sqlite3.connect('BDD.db')
                cur = con.cursor()
                cur.execute("select * from user where Pseudo=?",username.get())
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
                else:
                    cur.execute("insert into user(Psuedo,HashPassword) values(?,?)",(username.get(), password.get()))
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

    userentry = Entry(winsignup, width=40 , textvariable = username)
    userentry.focus()
    userentry.place(x=200 , y=223)

    passentry = Entry(winsignup, width=40, show="*" ,textvariable = password)
    passentry.place(x=200 , y=260)


    # button login and clear

    btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action)
    btn_signup.place(x=200, y=413)


    btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
    btn_login.place(x=280, y=413)


    sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
    sign_up_btn.place(x=350 , y =20)


    winsignup.mainloop()