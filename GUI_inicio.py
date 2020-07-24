from tkinter import *
import subprocess

#_____________________FUNCION INICIA CAMARA____________________________________
def onclick():
    subprocess.run('python Det_Camara.py', shell=True)

window=Tk()

#_____________________GUI________________________________________________________
btn=Button(window, text="Reconocimiento de rostros", fg='blue', command=onclick)
btn.place(x=80, y=100)
lbl=Label(window, text="Administrador", fg='red', font=("Helvetica", 16))
lbl.place(x=80, y=50)
window.title('Inicio')
window.geometry("300x200+600+100")
window.mainloop()