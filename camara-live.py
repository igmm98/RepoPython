from tkinter import messagebox
from imutils import paths
import subprocess
import cv2
import face_recognition
import os
import msgWhatsapp
import datetime
import saveUnknowns
import time
import connection
import smsMessage

#All images from file - Todas las imagenes dentro de la carpeta 'set'
#El nombre que recibe el rostro detectado es el nombre del archivo hasta donde haya un '_'
#EX: PeterParker_Spiderman, El rostro se llamara 'PeterParker'
encoding_conocidos = []
nombres_encoding = []

for filename in os.listdir('set/'):

    imagen_yo = face_recognition.load_image_file('set/{}'.format(filename))

    # Seccion de encuadre para informar a face_recognition que la imagen en su totalidad contiene el rostro
    # De otro modo face_recognition intenta detectar por partes en la imagen y genera error
    height, width, _ = imagen_yo.shape
    face_location = (0, width, height, 0)
    #
    encoding_personal = face_recognition.face_encodings(imagen_yo, known_face_locations=[face_location])[0]
    encoding_conocidos.append(encoding_personal)
    sub_index = filename.index('_')
    nombres_encoding.append(filename[0:sub_index])



# Set de imagenes - one by one
#imagen_yo = face_recognition.load_image_file('set\RUT19853982\one.JPG')
#encoding_personal = face_recognition.face_encodings(imagen_yo)[0]

#encoding_conocidos = [
#    encoding_personal
#]
#nombres_encoding = [
#    "19853982"
#]


cam = cv2.VideoCapture(0)


con = 0 # Cuenta Frames con "Conocidos" o "Desconocidos"
nombres_rostros = []

while True:

    ret_val, img = cam.read()

    if ret_val:

        
        # Escalamiento para optimizacion de lectura
        img_rgb = img[:, :, ::-1]
        img_rgb = cv2.resize(img_rgb, (0, 0), fx=1.0/5, fy=1.0/5)

        # Metodo para deteccion - cnn: Mayor presicion, mas lentitud - hog: Mayor velocidad, menos presicion
        ubi_rostro = face_recognition.face_locations(img_rgb, model="hog") 
        encodings_rostros = face_recognition.face_encodings(img_rgb, ubi_rostro)

        
        color = (0, 255, 0) # Verde por defecto / Bordes rostro
        
        nombres_rostros = []
        for encoding in encodings_rostros:
            nom = ""
            coincidencias = face_recognition.compare_faces(encoding_conocidos, encoding)
            
            if True in coincidencias:
                llamada = connection.callUsers()
                llamada.select_user(nombres_encoding[coincidencias.index(True)])
                nom = llamada.select_user(nombres_encoding[coincidencias.index(True)])
                #nom = nombres_encoding[coincidencias.index(True)]
                color = (0, 255, 0)
                con = 0
                    
            else:
                nom = "DESCONOCIDO"
                color = (0, 0, 255) #Se modifica color del recuadro para rostros desconocidos
                con += 1

            nombres_rostros.append(nom)
   

    for ((top, right, bottom, left), nom) in zip(ubi_rostro, nombres_rostros):
        
        # Alerta - Podria iniciar por timer o contador de Frames
        #EX1: Contar por segundos el tiempo que un rostro desconocido es detectado
        #EX2: En la imagen durante repetidos frames se detecta un desconocido
        if con>5:
            #messagebox.showwarning(message="Unknown user detected", title="Alert")
            dateNow = datetime.datetime.now()
            dateIs = dateNow.strftime("%b-%d-%Y__%H-%M")
            global name_SavedImg
            name_SavedImg = "unknown{}.jpg".format(dateIs)
            cv2.imwrite(name_SavedImg, img)
            saveUnknowns.UploadUnknowns(name_SavedImg)
            time.sleep(1)
            msgWhatsapp.SendAlert(name_SavedImg)
            #Envio de alerta sms al profe
            smsMessage.sendSMS()
            
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