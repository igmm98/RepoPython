from tkinter import *
import subprocess

#_____________________FUNCION INICIA CAMARA____________________________________
def onclick1():
    subprocess.run('python camara-live.py', shell=True)

def onclick2():
    subprocess.run('python save-path.py')
window=Tk()

#_____________________GUI________________________________________________________
btn=Button(window, text="Reconocimiento de rostros", fg='blue', command=onclick1)
btn.place(x=80, y=100)
btnn=Button(window, text="Generar set rostros", fg='blue', command=onclick2)
btnn.place(x=80, y=140)
lbl=Label(window, text="Administrador", fg='red', font=("Helvetica", 16))
lbl.place(x=80, y=50)
window.title('Inicio')
window.geometry("300x200+600+100")
window.mainloop()