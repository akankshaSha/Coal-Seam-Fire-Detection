## numpy basics

## How is it different from lists? 
# Numpy arrays are contigius and single typed

## Applications: 
#   1. MATLAB
#   2. Pandas, connect4, dip
#   3. ML

import numpy as np

#%% CREATE

## initialising numpy arrays
a = np.array([1, 2, 3], dtype='int16')
print(a)
b = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]])

# get dimesions .ndim
print(a.ndim)
print(b.ndim)

# get shape
print(a.shape)
print(b.shape)

# get type
print(a.dtype)
print(b.dtype)

# get total size
print(a.size)
print(b.size)
print(a.nbytes)

#%% READ / UPDATE

a = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]])

## get [row , col]
print(a[2, 3])
print(a[2, -1])

## get row / col
print(a[0, :])
print(a[:, 2])
print(a[0, 1:6:2])

## set [row, col]
a[2, 3] = 10
a[:, 2] = 5
print(a)

## set row / col
a[0, :] =  [10, 10, 10, 10, 10, 10, 10, 10, 10]
print(a)

#%% 3D ARRAYS

cube = np.array(
        [[[1, 1, 1], [2, 2, 2], [3, 3, 3]], 
        [[4, 4, 4], [5, 5, 5], [6, 6, 6]], 
        [[7, 7, 7], [8, 8, 8], [9, 9, 9]]]
        )
print(cube[1, 1, 1])
cube[1, 1, :] = [4, 5, 6]
print(cube)

#%% initializing different types of arrays

## all 0s
zero22 = np.zeros((2, 2))

## all 1s
one33 = np.ones((3, 3))

## all to something
all99 = np.full((2, 2), 99)

