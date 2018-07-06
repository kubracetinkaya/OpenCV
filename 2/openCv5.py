import cv2
import numpy as np

#siyah bir zemin olusturuyoruz.
img = np.zeros((512,512,3),np.uint8)


#5 piksel kalinliginda diagonal mavi bir cizgi cizdiriyoruz. Cizginin ozellikleri
#size kalmis, 8 bitlik degerleri istediginiz gibi degistirebilirsiniz.

cv2.line(img,(0,0),(511,511),(255,0,0),5) #cizgi cizimi

cv2.rectangle(img,(384,0),(510,511),(0,255,0),3) #diksortgen cizimi

cv2.circle(img,(447,63),63,(0,0,255),-1) #daire cizimi

cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1) #elips cizimi


#poligon cizimi
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts],False,(0,255,255))


#beyaz renkte 'Sekiller' yazdiracagiz
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Sekiller',(10,500),font,4,(255,255,255),2,cv2.LINE_AA)

#goruntunun olusturuldugu pencereyi kapatmak icin herhangi bi tusu bekle
cv2.imshow('Geometrik Sekiller',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




