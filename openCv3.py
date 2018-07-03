import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('saat.jpg',0)
cv2.imwrite('saat.png',img)
