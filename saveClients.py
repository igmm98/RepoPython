from tkinter import *
from tkinter import messagebox
import connection


def main_account_screen():

    
    
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("400x300+600+100") # set the configuration of GUI window 
    main_screen.title("Registar cliente") # set the title of GUI window
 
# create a Form label 
    Label(text="Ingresar cliente", bg="white", width="300", height="2", font=("Calibri", 11)).pack() 
    Label(text="").pack() 

    
    rut_lable = Label(main_screen, text="Rut")
    rut_lable.pack()
 

# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    rut = StringVar()
    rut_entry = Entry(main_screen, textvariable=rut, width="35" )
    rut_entry.pack()

    
    nombre_lable = Label(main_screen, text="Nombre")
    nombre_lable.pack()
 

# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    nombre = StringVar()
    nombre_entry = Entry(main_screen, textvariable=nombre, width="35" )
    nombre_entry.pack()

    apellido_lable = Label(main_screen, text="Apellido")
    apellido_lable.pack()
 

# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    apellido = StringVar()
    apellido_entry = Entry(main_screen, textvariable=apellido, width="35" )
    apellido_entry.pack()

    fono_lable = Label(main_screen, text="Fono")
    fono_lable.pack()
 

# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    fono = IntVar()
    fono_entry = Entry(main_screen, textvariable=fono, width="35" )
    fono_entry.pack()

    def onclick():
        #print("noice")
        llamada = connection.callUsers()
        llamada.insert_cliente(rut.get(), nombre.get(), apellido.get(), fono.get())
        main_screen.destroy()
 
# create Login Button 
    Label(text="").pack()
    Button(text="Guardar", height="2", width="30", command=onclick).pack() 
 
    main_screen.mainloop() # start the GUI
 
main_account_screen() # call the main_account_screen() function