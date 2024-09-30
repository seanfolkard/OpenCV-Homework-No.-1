# Folkard, Sean Michael - OpenCV Homework No. 1

import os
import cv2

# Load the image
image_path = os.path.join('pics/hanni-new-jeans.jpg')
img = cv2.imread(image_path)

new_width = int(img.shape[1] * 0.5)
new_height = int(img.shape[0] * 0.5)
new_dim = (new_width, new_height)

resized_img = cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cropped_img_rgb = img_rgb[120:450, 320:700]
cropped_img_hsv = img_hsv[120:450, 320:700]

print(img.shape)
print(resized_img.shape)

cv2.imshow('Original', img)
cv2.imshow('Scaled by 50%', resized_img)
cv2.imshow("Cropped RGB", cropped_img_rgb)
cv2.imshow("Cropped HSV", cropped_img_hsv)

cv2.waitKey(0)