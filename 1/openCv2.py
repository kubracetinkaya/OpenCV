import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('WALL-E.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,100],[80,500],'c',linewidth=5)
plt.show()
