import cv2

faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#ACTIVAR CAPTURA DE VIDEO OPENCV
cam = cv2.VideoCapture(0)

while True:
    
    ret_val, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #RANGOS DE MEDICION
    faces = faceClassif.detectMultiScale(gray,
    scaleFactor=1.1,
    minNeighbors=20,
    minSize=(10,10),
    maxSize=(200,200))

    #ENMARCAR ROSTRO
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0, 255, 0),2)

    #RECUADRO
    cv2.imshow('Camara en vivo', img)   

    if cv2.waitKey(1) == 27:  
        break  # esc to quit    
cv2.destroyAllWindows()