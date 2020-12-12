from tkinter import *
import time
import connection
from tkinter import messagebox


def main_account_screen():
    
    main_screen = Tk()   # create a GUI window 
    main_screen.resizable(False, False)
    main_screen.geometry("300x220+600+100") # set the configuration of GUI window 
    main_screen.title("Registro de  fotografias") # set the title of GUI window
 
    # create a Form label 
    Label(text="RUT", bg="white", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 

    # 
    name = StringVar()
    fileName_lable = Label(main_screen, text="Rut cliente")
    fileName_lable.pack()

    fileName_entry = Entry(main_screen, textvariable=name)
    fileName_entry.pack()
 
    spare_lable = Label(main_screen, text=" ")
    spare_lable.pack()

    # create a register button
    

    def saveRut():
        global rut
        rut = name.get()

        llamada = connection.callUsers()
        if llamada.select_user(rut)=="ERROR":
            messagebox.showerror("Alerta","Rut invalido")

        else:
            time.sleep(1)
            main_screen.destroy()

    Button(text="Register", height="2", width="30", command=saveRut).pack()

    main_screen.mainloop() # start the GUI
 
main_account_screen() # call the main_account_screen() function

