#%% 1. imports
import numpy as np
import cv2
from skimage import io
import pandas as pd

from util.imageConstructor import construct
from util.marker import Marker


#%% 2. read images
band8 = io.imread("data/2019-12-19/B8.tiff")
band11 = io.imread("data/2019-12-19/B11.tiff")
band12 = io.imread("data/2019-12-19/B12.tiff")


#%% 3. construct image

for row in range(band8.shape[0]):
    for col in range(band8.shape[1]):
        if band8[row, col] == 0:
            band8[row, col] = 1

thermal_img = (band11 - band12) / band8;

x = 255 / thermal_img.max()
thermal_img = thermal_img * x;

img = construct(thermal_img, thermal_img, thermal_img)
shape = img.shape



#%% 4. resizing and converting images
img = img.reshape((-1, 3))
img = np.float32(img)


#%% 5. clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 4
attempts = 10
ret,label,center = cv2.kmeans(img,k,None,criteria,attempts,cv2.KMEANS_RANDOM_CENTERS)

#%% 6. coverting back to uint8

center = np.uint8(center)
res = center[label.flatten()]
res = res.reshape((shape))
#cv2.imwrite('results/K2.tiff', res)

#%% loading fire / no fire pixels

validation = pd.read_excel('data/2019-12-19/validation.xlsx')
bottomLeft = (23.623, 86.148)

marker = Marker(res, validation, bottomLeft)
marker.mark(5, (0, 0, 255), (0, 255, 0))

cv2.imwrite('results/Thrmal Img K'+ str(k) +'.tiff', res)
