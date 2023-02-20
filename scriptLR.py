#%% 1. imports

from skimage import io
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#%% 2. read images

band4 = io.imread('2023-02-16/B4.tiff')
band8 = io.imread('2023-02-16/B8.tiff')
band11 = io.imread('2023-02-16/B11.tiff')
band12 = io.imread('2023-02-16/B12.tiff')
marked = io.imread('2023-02-16/marked.tiff')


#%% 3. make a datafram from images

df_img = pd.DataFrame(columns=['band4', 'band8', 'band11', 'band12', 'hasFire'])

count = 0
for i in range(marked.shape[0]):
    for j in range(marked.shape[1]):
        if marked[i, j, 0] == 255 and marked[i, j, 1] == 0 and marked[i, j, 2] == 0:
            df_img.loc[count] = [band4[i, j], band8[i, j], band11[i, j], band12[i, j], True]
            count += 1
        elif marked[i, j, 0] == 0 and marked[i, j, 1] == 255 and marked[i, j, 2] == 0:
            df_img.loc[count] = [band4[i, j], band8[i, j], band11[i, j], band12[i, j], False]
            count += 1
            
            
#%%
#df_img.to_csv('pixel_fire.csv', index = False)
plt.scatter(df_img.band4, df_img.hasFire)
plt.scatter(df_img.band8, df_img.hasFire)
plt.scatter(df_img.band11, df_img.hasFire)
plt.scatter(df_img.band12, df_img.hasFire)


#%% 4. test - traon split

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

B8 = io.imread('Jharia/B8.tiff')
B11 = io.imread('Jharia/B11.tiff')
B12 = io.imread('Jharia/B12.tiff')

img = np.zeros((B8.shape[0], B8.shape[1], 3), dtype='uint8')

for row in range(0, img.shape[0]):
    for col in range(0, img.shape[1]):
        X = [[B8[row, col], B11[row, col], B12[row, col]]]
        if(model.predict(X)):
            img[row, col, 0] = 255

io.imshow(img)