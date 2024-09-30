# resizing
import os
import cv2

# Load the image
image_path = os.path.join("pics/new-    jeans.jpg")
img = cv2.imread(image_path)

new_width = int(img.shape[1] * 0.5)
new_height = int(img.shape[0] * 0.5)
new_dim = (new_width, new_height)

resized_img = cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA)

print(img.shape)
print(resized_img.shape)

cv2.imshow('Original', img)
cv2.imshow('Scaled by 50%', resized_img)

cv2.waitKey(0)