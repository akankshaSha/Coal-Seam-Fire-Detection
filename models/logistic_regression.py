#%% 1. imports

from skimage import io
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from util.marker import Marker


#%% 2. read images

band8 = io.imread('data/2019-12-19/B8.tiff')
band11 = io.imread('data/2019-12-19/B11.tiff')
band12 = io.imread('data/2019-12-19/B12.tiff')
marked = io.imread('data/2019-12-19/marked.tiff')


#%% 3. make a datafram from images

df_img = pd.DataFrame(columns=['band8', 'band11', 'band12', 'hasFire'])

count = 0
for i in range(marked.shape[0]):
    for j in range(marked.shape[1]):
        if marked[i, j, 0] == 255 and marked[i, j, 1] == 0 and marked[i, j, 2] == 0:
            df_img.loc[count] = [band8[i, j], band11[i, j], band12[i, j], True]
            count += 1
        elif marked[i, j, 0] == 0 and marked[i, j, 1] == 255 and marked[i, j, 2] == 0:
            df_img.loc[count] = [band8[i, j], band11[i, j], band12[i, j], False]
            count += 1
            

#%% 4. test - train split

from sklearn.model_selection import train_test_split

X = df_img[['band8', 'band11', 'band12']]
Y = df_img['hasFire']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3)


#%% training

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, Y_train)


#%% testing

print(model.score(X_test, Y_test))


#%% construct fire map for full images

img = np.zeros((band8.shape[0], band8.shape[1], 3), dtype='uint8')

for row in range(0, img.shape[0]):
    for col in range(0, img.shape[1]):
        X = [[band8[row, col], band11[row, col], band12[row, col]]]
        if(model.predict(X)):
            img[row, col, 0] = 255

io.imshow(img)


#%% mark validation points

validation = pd.read_excel('data/2019-12-19/validation.xlsx')
bottomLeft = (23.623, 86.148)
marker = Marker(img, validation, bottomLeft)

marked = marker.mark(5, (255, 255, 0), (0, 0, 255))
plt.imsave('results/logistic_regression.tiff', img)