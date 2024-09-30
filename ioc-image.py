import os
import cv2

# read image
image_path = os.path.join('pics\smiski.jpg')
img = cv2.imread(image_path)

# write image (save a copy)
#cv2.imwrite(os.path.join('.', 'pics', 'shibainu1_out.jpg'), img)

# visualize/display image 
cv2.imshow('Original', img)
cv2.waitKey(0)


