import numpy as np

def construct(greyscale1, greyscale2, greyscale3):
    '''

    Parameters
    ----------
    greyscale1 : uint8 numpy array
        grey scale image converted to red
    greyscale2 : uint8 numpy array
        grey scale image converted to yellow
    greyscale3 : uint8 numpy array
        grey scale image converted to red

    Returns
    -------
    cinstructe image

    '''
    img = np.zeros((greyscale3.shape[0], greyscale3.shape[1], 3), dtype='uint8')

    for row in range(0, img.shape[0]):
        for col in range(0, img.shape[1]):
            img[row, col, 0] = greyscale1[row, col]
            img[row, col, 1] = greyscale2[row, col]
            img[row, col, 2] = greyscale3[row, col]
    
    return img