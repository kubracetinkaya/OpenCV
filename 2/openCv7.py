import numpy as np
import cv2

#resmimizin uzeerine geometrik sekiller cizecegiz.
img = cv2.imread('WALL-E.jpg', cv2.IMREAD_COLOR)

# 2 piksel kalınlığında diagonal mavi bir çizgi çizdiriyoruz. Çizginin özellikleri size kalmış, 8 bitlik değerleri istediğiniz gibi değiştirebilirsiniz.

cv2.line(img,(0,0),(150,150),(255,0,0),2)

# Dikdörtgen Çizimi:
cv2.rectangle (img,(350,0), (200,200), (0,255,0), 3)

# Daire Çizimi:
cv2.circle (img,(300,400),63,(0,0,255),-1)

# Elips Çizimi:
cv2.ellipse(img,(200,255), (100,50),0,0,180,255,-1)

# Poligon Çizimi:

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

#Mavi renkte 'WALL-E' yazdıracağız.
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'WALL-E', (0,375), font, 4, (255,0,0),2,cv2.LINE_AA)


cv2.imshow('Geometrik-Sekiller',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
