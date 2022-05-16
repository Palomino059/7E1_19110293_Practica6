import cv2
import numpy as np

cap = cv2.VideoCapture(0)

redBajo1 = np.array([0,100,20],np.uint8)#Determinar el rango de color rojo
redAlto1 = np.array([8,255,255],np.uint8)

redBajo2 = np.array([175,100,20],np.uint8)
redAlto2 = np.array([179,255,255],np.uint8)

greenBajo = np.array([40,100,20],np.uint8)
greenAlto = np.array([75,255,255],np.uint8)

BlueBajo = np.array([100,100,20],np.uint8)
BlueAlto = np.array([135,255,255],np.uint8)

while True:
    ret, frame = cap.read()
    if ret == True:
        # Parte de HSV  
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskRed1 = cv2.inRange(frameHSV,redBajo1,redAlto1)# Encontrar la imagen del color
        maskRed2 = cv2.inRange(frameHSV,redBajo2,redAlto2)# Encontrar la imagen del color
        maskGreen = cv2.inRange(frameHSV,greenBajo,greenAlto)
        maskBlue = cv2.inRange(frameHSV,BlueBajo,BlueAlto)

        maskRed = cv2.add(maskRed1,maskRed2)# Para convertir en una sola mascara

        maskRGB = maskRed1 + maskRed2 + maskGreen + maskBlue 
        
        maskRedvis = cv2.bitwise_and(frame,frame, mask = maskRed)# Antes de mostrar en balnco la imagen la convierte a color que corresponde
        maskBluevis = cv2.bitwise_and(frame,frame, mask = maskBlue)
        maskGreenvis = cv2.bitwise_and(frame,frame, mask = maskGreen)

        
        maskRGBvis = maskRedvis +  maskBluevis + maskGreenvis
        print(maskRGB)

        "------- Rojo ---------"
        #cv2.imshow('maskRedvis',maskRedvis)
        #cv2.imshow('maskRed',maskRed)

        "------- Azul --------"
        #cv2.imshow('maskBluevis',maskBluevis)
        #cv2.imshow('maskBlue',maskBlue)

        "-------- Verde -------"
        #cv2.imshow('maskGreenvis',maskGreenvis)
        #cv2.imshow('maskGreen',maskGreen)

        "--------- RGB----------"
        cv2.imshow('maskRGBvis',maskRGBvis)
        cv2.imshow('maskRGB',maskRGB)
        
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break

cap.release()
cv2.destroyAllWindows() 

      
