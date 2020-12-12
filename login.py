from tkinter import *
from tkinter import messagebox
import connection


def main_account_screen():

    
    
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("300x250+600+100") # set the configuration of GUI window 
    main_screen.title("Account Login") # set the title of GUI window
 
# create a Form label 
    Label(text="Ingresar", bg="white", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 

    # Set username label
    username_lable = Label(main_screen, text="Username")
    username_lable.pack()
 
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    username = StringVar()
    username_entry = Entry(main_screen, textvariable=username, width="35" )
    username_entry.pack()

    # Set password label
    password_lable = Label(main_screen, text="Password")
    password_lable.pack()
 
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    password = StringVar()
    password_entry = Entry(main_screen, textvariable=password, show='*', width="35" )
    password_entry.pack()

    def onclick():
        llamada = connection.callUsers()
        if llamada.user_validation(username.get(), password.get())=="":
            messagebox.showwarning("Alerta", "Incorrecto")
        else:
            main_screen.destroy()
 
# create Login Button 
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=onclick).pack() 
 
    main_screen.mainloop() # start the GUI
 
main_account_screen() # call the main_account_screen() function