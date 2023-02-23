#%% 1. imports
import numpy as np
import cv2
from skimage import io
from util.imageConstructor import construct


#%% 2. read images
band8 = io.imread("data/2019-12-19/B8.tiff")
band11 = io.imread("data/2019-12-19/B11.tiff")
band12 = io.imread("data/2019-12-19/B12.tiff")


#%% 3. construct image

img = construct(band8, band11, band12)
shape = img.shape


#%% 4. resizing and converting images
img = img.reshape((-1, 3))
img = np.float32(img)


#%% 5. clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 2
attempts = 10
ret,label,center = cv2.kmeans(img,k,None,criteria,attempts,cv2.KMEANS_RANDOM_CENTERS)

#%% 6. coverting back to uint8

center = np.uint8(center)
res = center[label.flatten()]
res = res.reshape((shape))
cv2.imwrite('2019-12-19/segmented/K2.tiff', res)