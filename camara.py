import cv2
import face_recognition

faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

imagen_yo = face_recognition.load_image_file('set\one.JPG')
imagen_yo2 = face_recognition.load_image_file('set\one2.JPG')
imagen_yo3 = face_recognition.load_image_file('set\one3.JPG')
encoding_personal = face_recognition.face_encodings(imagen_yo)[0]
encoding_personal1 = face_recognition.face_encodings(imagen_yo2)[0]
encoding_personal2 = face_recognition.face_encodings(imagen_yo3)[0]

encoding_conocidos = [
    encoding_personal,
    encoding_personal1,
    encoding_personal2
]
nombres_encoding = [
    "IGNACIO",
    "IGNACIO",
    "IGNACIO"
]

texto = cv2.FONT_HERSHEY_COMPLEX

reduc = 5

#ACTIVAR CAPTURA DE VIDEO OPENCV
cam = cv2.VideoCapture(0)

while True:

    ubi_rostro = []
    encoding_rostros = []
    nombres_rostros = []
    nom = ""
    
    ret_val, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #-------------------------------------------
    img_rgb = img[:, :, ::-1]
    img_rgb = cv2.resize(img_rgb, (0, 0), fx=1.0/reduc, fy=1.0/reduc)
    #-------------------------------------------
    ubi_rostro = face_recognition.face_locations(img_rgb)
    encodings_rostros = face_recognition.face_encodings(img_rgb, ubi_rostro)
    #-------------------------------------------
    for encoding in encodings_rostros:
        coincidencias = face_recognition.compare_faces(encoding_conocidos, encoding)

        if True in coincidencias:
            nom = nombres_encoding[coincidencias.index(True)]
        else:
            nom = "DESCONOCIDO"

        nombres_rostros.append(nom)

    #RANGOS DE MEDICION
    faces = faceClassif.detectMultiScale(gray,
    scaleFactor=1.1,
    minNeighbors=10,
    minSize=(10,10),
    maxSize=(200,200))

    #ENMARCAR ROSTRO
    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(0, 255, 0),2)
        cv2.putText(img, nom, (x, y - 6), texto, 0.6, (255,255,255), 1)

    

    #RECUADRO
    cv2.imshow('Camara en vivo', img)   

    if cv2.waitKey(1) == 27:  
        break  # esc to quit    
cv2.destroyAllWindows()