import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('saat.jpg', 0)

#cv2.IMREAD_GRAYSCALE = 0
#cv2.IMREAD_COLOR = 1
#cv2.IMREAD_UNCHANGED = -1


cv2.imshow('image',img)
cv2.waitkey()
cv2.destroyAllWindows()
