from tkinter import *
import subprocess
import login

#_____________________FUNCION INICIA CAMARA____________________________________
def onclick1():
    subprocess.run('python camara-live.py', shell=True)

def onclick2():
    subprocess.run('python save-path.py')

def onclick3():
    subprocess.run('python saveClients.py')



window=Tk()

#_____________________GUI________________________________________________________
btn=Button(window, text="Reconocimiento de rostros", fg='blue', width="25", command=onclick1)
btn.place(x=60, y=100)
btnn=Button(window, text="Registrar rostro", fg='blue', width="25", command=onclick2)
btnn.place(x=60, y=140)
btnn=Button(window, text="Registrar cliente", fg='blue', width="25", command=onclick3)
btnn.place(x=60, y=180)
lbl=Label(window, text="Administrador", fg='red', font=("Helvetica", 16))
lbl.place(x=85, y=50)
window.title('Inicio')
window.resizable(False, False)
window.geometry("300x250+600+100")
window.mainloop()