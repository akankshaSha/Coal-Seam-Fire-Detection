#%% 1. imports

from skimage import io
import matplotlib.pyplot as plt
import pandas as pd


#%% function definations

def getPixel(bottomLeft, csResolution, shape, lat, lon):
    x = (lat - bottomLeft[0]) // csResolution[0]
    y = (lon - bottomLeft[1]) // csResolution[1]
    return (shape[0] - int(x), int(y))


def mark(img, br):
    img[br[0], br[1], 0] = 255
    img[br[0], br[1], 1] = 0
    img[br[0], br[1], 2] = 0
    for i in range(10):
        for j in range(10):
            try:
                img[br[0] - i, br[1] - j, 0] = 255
                img[br[0] - i, br[1] - j, 1] = 0
                img[br[0] - i, br[1] - j, 2] = 0
            except:
                break


#%% 2. inputs

# a) image

band4 = io.imread('2019-12-19/B4.tiff')
band8 = io.imread('2019-12-19/B8.tiff')
band11 = io.imread('2019-12-19/B11.tiff')
band12 = io.imread('2019-12-19/B12.tiff')
swir = io.imread('2019-12-19/SWIR.tiff')

# b) latitude / longitude of the top left cornor of the image

bottomLeft = (23.623, 86.148)

# c) cordinate system resolution (latitude degree pp, longitude degree pp)

csResolution = (0.0002358, 0.0002576)

# d) read dataframe

validation = pd.read_excel('2019-12-19/validation.xlsx')

# e) latitude / longitudes of points of interest
pois = []
for index, row in validation.iterrows():
    pois.append((validation['lat'][index], validation['lon'][index]))

#%% Mark on SWIR

for poi in pois:
    br = getPixel(bottomLeft, csResolution,  swir.shape, poi[0], poi[1])
    #print(br)
    mark(swir, br)

plt.imsave('2019-12-19/marked.tiff', swir)
