import cv2
import numpy as np

img=cv2.imread('WALL-E.jpg',0)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27:  #ESC tusunu bekler.
    cv2.destroyAllWindows()
elif k==ord('s'):  #Kayit icin 's' tusunu bekler.
    cv2.imwrite('WALL-E.png',img)
    cv2.destroyAllWindows()
