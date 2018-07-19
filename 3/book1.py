
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help='Path to the image')
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
print("width: %d pixels" % (image.shape[1])) #goruntunun boyutlarini inceler
print("height: %d pixels" % (image.shape[0]))#bu incelemeyi shape ile yapar
print("channels: %d" % (image.shape[2]))


cv2.imshow("image",image)
cv2.waitKey(0)
cv2.imwrite("newimage.jpg",image)


