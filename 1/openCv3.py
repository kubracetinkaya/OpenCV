import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('WALL-E.jpg',0)
cv2.imwrite('WALL-E.png',img)
