import cv2
import savePhotos
import connection

faceClassif =   cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.XML')

indice = 1
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

        image = '{}_{}.jpg'.format(savePhotos.rut, indice)

        llamada = connection.callUsers()
        #print(llamada.id_user(savePhotos.rut))
        llamada.insert_photo(image, llamada.id_user(savePhotos.rut))
        
        try:
            cv2.imwrite('set\{}'.format(image), rostro)
        except Exception as e:
            print("Registro existente")
        indice+=1

    cv2.imshow('Recoleccion rostros', f)

    if cv2.waitKey(1) == 27 or indice>10:
        break  # Esc to quit  
vid.release()

cv2.destroyAllWindows()