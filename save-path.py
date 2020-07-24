from imutils import paths
import cv2
import os

faceClassif =   cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.XML')

indice = 0
vid = cv2.VideoCapture(0)

while True:
    v, f = vid.read()
    f = cv2.flip(f, 1)
    auxF = cv2.flip(f, 1)

    faces = faceClassif.detectMultiScale(f, 1.3, 5)
    
    for (x,y,w,h) in faces:

        cv2.rectangle(f, (x,y), (x+w,y+h), (128,0,255), 2)
        rostro = f[y:y+h,x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        

        cv2.imwrite('set\desconocido_{}.jpg'.format(indice), rostro)
        indice+=1

    cv2.imshow('Recoleccion rostros', f)

    if cv2.waitKey(1) == 27 or indice>300:
        break  # Esc to quit  
vid.release()

cv2.destroyAllWindows()