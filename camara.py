import cv2
import os
import imutils
import numpy as np

nameCarpeta= 'set'
dataPath = 'C:/Users/mr_ig/Desktop/deteccion_rostros/RepoPyhton'
dirr = nameCarpeta + '/' + dataPath


faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    count = 0
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            auxFrame = img.copy()

            faces = faceClassif.detectMultiScale(gray,
                scaleFactor=1.1,
                minNeighbors=20,
                minSize=(10,10),
                maxSize=(200,200))

            for (x,y,w,h) in faces:

                cv2.rectangle(img,(x,y),(x+w,y+h),(0, 255, 0),2)
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(dirr + '/rostro_{}.jpg'.format(count),rostro)
                count = count + 1

        cv2.imshow('Camara en vivo', img)

        if cv2.waitKey(1) == 27 or count >=300: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()