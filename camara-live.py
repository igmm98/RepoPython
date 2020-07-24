from tkinter import messagebox
import subprocess
import cv2
import face_recognition

# Set de imagenes
imagen_yo = face_recognition.load_image_file('set\one.JPG')
encoding_personal = face_recognition.face_encodings(imagen_yo)[0]

encoding_conocidos = [
    encoding_personal
]
nombres_encoding = [
    "IGNACIO"
]

cam = cv2.VideoCapture(0)


con = 0 # Cuenta Frames
nombres_rostros = []

while True:

    ret_val, img = cam.read()

    if ret_val:
        
        # Escalamiento para optimizacion de lectura
        img_rgb = img[:, :, ::-1]
        img_rgb = cv2.resize(img_rgb, (0, 0), fx=1.0/5, fy=1.0/5)

        # Metodo para deteccion - cnn: Mayor presicion, mas lentitud - hog: Mayor velocidad, menos presicion
        ubi_rostro = face_recognition.face_locations(img_rgb, model="cnn") 
        encodings_rostros = face_recognition.face_encodings(img_rgb, ubi_rostro)

        
        color = (0, 255, 0) # Verde por defecto / Bordes rostro
        
        nombres_rostros = []
        for encoding in encodings_rostros:
            nom = ""
            coincidencias = face_recognition.compare_faces(encoding_conocidos, encoding)
            
            if True in coincidencias:
                nom = nombres_encoding[coincidencias.index(True)]
                color = (0, 255, 0)
                con = 0
                    
            else:
                nom ="DESCONOCIDO"
                color = (0, 0, 255)
                con += 1

            nombres_rostros.append(nom)
   

    for ((top, right, bottom, left), nom) in zip(ubi_rostro, nombres_rostros):

        # Alerta - Puede ser timer o contador de Frames
        if con>5:
            messagebox.showwarning(message="Unknown user detected", title="Alert")
            cv2.imwrite('desconocido.jpg', img)
            subprocess.run('python WhatsappMessage.py', shell=True)
            con = 0
        
        
        # Re-escalamiento
        top = int(top * 5)
        right = int(right * 5)
        bottom = int(bottom * 5)
        left = int(left * 5)

        # Rectangulo y nombre
        cv2.rectangle(img, (left, top), (right, bottom), color, 2)
        cv2.putText(img, nom, (left, bottom + 20), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255), 1)

    cv2.imshow('Live', img) # Imagen

    if cv2.waitKey(1) == 27:  
        break  # Esc - Salir

cv2.destroyAllWindows()