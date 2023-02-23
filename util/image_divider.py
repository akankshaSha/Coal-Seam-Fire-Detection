class ImageDivider:
    
    
    def __init__(self, img):
        '''
        Parameters
        ----------
        img : numpy array

        Returns
        -------
        Object

        '''
        self.img = img
    
    
    def divider(self, stride):
        '''        
        Parameters
        ----------
        stride : tuple
            (height, width) of the intended block size

        Returns
        -------
        list of blocks
        '''
        res = []
        
        for i in range(0, self.img.shape[0], stride[0]):
            for j in range(0, self.img.shape[1], stride[1]):
                res.append(self.img[i : i + stride[0], j : j + stride[1], :])
                
        return res
    
    
    def tailor(self, blocks):
        '''
        Parameters
        ----------
        blocks : list
            list of blocks to be tailores

        Returns
        -------
        image
        '''
        stride = blocks[0].shape
        res = self.img
        k = 0
        
        for i in range(0, res.shape[0], stride[0]):
            for j in range(0, res.shape[1], stride[1]):
                I = i + stride[0] if i + stride[0] < res.shape[0] else res.shape[0]
                J = j + stride[1] if j + stride[1] < res.shape[1] else res.shape[1]
                res[i : I, j : J] = blocks[k]
                k += 1
                if k == len(blocks):
                    return res
                
        return res
    
    
#%% example usage

# =============================================================================
# from skimage import io
# 
# img = io.imread('Learning/image1.jpg')
# 
# # initialize object with image
# imd = ImageDivider(img)
# 
# # dividing image
# tiles = imd.divider((75, 75))
# 
# # tailoring image
# i = imd.tailor(tiles)
# =============================================================================

