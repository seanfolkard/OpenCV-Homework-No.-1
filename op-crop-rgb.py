# crop
import os
import cv2

image_path = os.path.join("pics/new-jeans.jpg")
img = cv2.imread(image_path)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cropped_img = img[220:740, 320:940]

cv2.imshow("img", img)
cv2.imshow("Cropped RGB", img_rgb)
cv2.waitKey(0)