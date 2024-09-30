# crop
import os
import cv2

image_path = os.path.join("pics\smiski.jpg")
img = cv2.imread(image_path)

print(img.shape)
cropped_img = img[220:740, 320:940]

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)