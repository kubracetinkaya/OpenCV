import cv2
import numpy as np
import argparse
import imutils

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='Path to the image')
args=vars(ap.parse_args())

image=cv2.imread(args['image'])
cv2.imshow('Original',image)

r=150.0/image.shape[1]
dim=(150,int(image.shape[0]*r))

resized=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
cv2.imshow('Resized (width)',resized)

r=50.0/image.shape[0]
dim=(int(image.shape[1]*r),50)

resized=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
cv2.imshow('Resized (Height)',resized)
cv2.waitKey(0)

resized=imutils.resize(image,width=100)
cv2.imshow('Resized via functions',resized)
cv2.waitKey(0)
