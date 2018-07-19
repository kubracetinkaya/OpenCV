import cv2
import numpy as np

canvas=np.zeros((300,300,3),dtype='uint8') 
green=(0,255,0)
cv2.line(canvas,(0,0),(300,300),green)  #yesil bir cizgi ciziyor
cv2.imshow('Canvas',canvas)
cv2.waitKey(0)

red=(0,0,255)
cv2.line(canvas,(300,0),(0,300),red,3) #3 kalinliginda kirmizi bir cizgi ciziyor
cv2.imshow('Canvas',canvas)
cv2.waitKey(0)

cv2.rectangle(canvas,(10,10),(60,60),green) #yesil bir dikdortgen olusturuyor
cv2.imshow('Canvas',canvas)
cv2.waitKey(0)

cv2.rectangle(canvas,(50,200),(200,225),red,5) #5 kalinliginda kirmizi dikdortgen olusturuyor
cv2.imshow('Canvas',canvas)
cv2.waitKey(0)

blue=(255,0,0)
cv2.rectangle(canvas,(200,50),(225,125),blue,-1) #- parametresinden dolayi ici dolu mavi diksortgen ciziyor
cv2.imshow('Canvas',canvas)
cv2.waitKey(0)






    

