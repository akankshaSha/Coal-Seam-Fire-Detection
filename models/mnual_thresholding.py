#%% imports
from skimage import io
import numpy as np
import pandas as pd

from util.marker import Marker


#%% load images
band8 = io.imread('data/2019-12-19/B8.tiff')
band11 = io.imread('data/2019-12-19/B11.tiff')
band12 = io.imread('data/2019-12-19/B12.tiff')


#%% constructing image for thresholding

for row in range(band8.shape[0]):
    for col in range(band8.shape[1]):
        if band8[row, col] == 0:
            band8[row, col] = 1

thermal_img = (band11 - band12) / band8;

#%% setting different threshold

img = np.zeros((thermal_img.shape[0], thermal_img.shape[1], 3))

threshold = 0.625

for row in range(0, band8.shape[0]):
    for col in range(0, band8.shape[1]):
        if(thermal_img[row, col] > threshold):
            img[row, col, :] = 255
        else:
            img[row, col, :] = thermal_img[row, col]


#%% marking validation points

validation = pd.read_excel('data/2019-12-19/validation.xlsx')
bottomLeft = (23.623, 86.148)

marker = Marker(img, validation, bottomLeft)
marked = marker.mark(10, (255, 0, 0), (0, 255, 0))

io.imsave('results/threshold' + str(threshold) + '.jpg', marked)