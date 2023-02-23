#%% 1. imports
import numpy as np
import cv2


#%% 2. read images
img1 = cv2.imread('image1.jpg')
shape1 = img1.shape


#%% 3. resizing and converting images
img1 = img1.reshape((-1, 3))
img1 = np.float32(img1)


#%% 4. clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 5
attempts = 10
ret,label,center = cv2.kmeans(img1,k,None,criteria,attempts,cv2.KMEANS_RANDOM_CENTERS)

#%% 3. coverting back to uint8

center = np.uint8(center)
res = center[label.flatten()]
res = res.reshape((shape1))
cv2.imwrite('segmented2.jpg', res)