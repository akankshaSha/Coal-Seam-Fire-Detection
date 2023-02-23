#%% imports
from skimage import io
import matplotlib.pyplot as plt


#%% load images
band8 = io.imread('data/2019-12-19/B8.tiff')
band11 = io.imread('data/2019-12-19/B11.tiff')
band12 = io.imread('data/2019-12-19/B12.tiff')
marked = io.imread('data/2019-12-19/marked.tiff')


#%% constructing image for thresholding

for row in range(band8.shape[0]):
    for col in range(band8.shape[1]):
        if band8[row, col] == 0:
            band8[row, col] = 1

img = (band11 - band12) / band8;

#%% setting different threshold

threshold = 2.5

for row in range(0, band8.shape[0]):
    for col in range(0, band8.shape[1]):
        if(img[row, col] > threshold):
            img[row, col] = 255

plt.imsave('results/threshold' + str(threshold) + '.jpg', img)
