class Marker:
    
    def __init__(self, mapImage, validationData, bottomLeft, csResolution = (0.0002358, 0.0002576)):
        '''
        Parameters
        ----------
        mapImage : uint8 numpy array
            image of the map to be marked
        validationData : dataframe 
            validation data fram with headers 'lat' 'lon' 'hasFire'
            lat -> latitude (float64) 
            lon -> longitude (float64)
            hasFire -> if the point has Fire (boolean)
        bottomLeft : tuple
            (latitude, longitude) of the bottom left corner of the map
        csResolution : Tuple, optional
            cordinate system resolution (latitude degree per pixel, longitude degree perpixel).
            The default is (0.0002358, 0.0002576) from WSG84(EPSG:4326).
        Returns
        -------
        Object
        '''
        self.mapImage = mapImage
        self.validationData = validationData
        self.bottomLeft = bottomLeft
        self.csResolution = csResolution
        
        
    def __getPixel__(self, lat, lon):
        x = (lat - self.bottomLeft[0]) // self.csResolution[0]
        y = (lon - self.bottomLeft[1]) // self.csResolution[1]
        return (self.mapImage.shape[0] - int(x), int(y))
    
    
    def __getPoints__(self):
        for index, row in self.validationData.iterrows():
            yield((self.validationData['lat'][index], self.validationData['lon'][index], self.validationData['hasFire'][index]))

    
    def __mark__(self, offset, p, color):
        for i in range(offset):
            for j in range(offset):
                try:
                    self.mapImage[p[0] - i, p[1] - j, 0] = color[0]
                    self.mapImage[p[0] - i, p[1] - j, 1] = color[1]
                    self.mapImage[p[0] - i, p[1] - j, 2] = color[2]
                except:
                    break

    def get_fire_pixels(self):
        res = []
        for poi in self.__getPoints__():
            p = self. __getPixel__(poi[0], poi[1])
            if(poi[2]):
                res.append((p[0], p[1]))
        return res
    
   
    def get_no_fire_pixels(self):
        res = []
        for poi in self.__getPoints__():
            p = self. __getPixel__(poi[0], poi[1])
            if(not poi[2]):
                res.append((p[0], p[1]))
        return res
                
    def mark(self, offset, fire, noFire):
        '''
        Parameters
        ----------
        offset : int
            offset of the pixels
        fire : tuple
            (r, g, b) values of color of fire pixel
        noFire : tuple
            (r, g, b) values of color of non fire pixel

        Returns
        -------
        image (numpy array)
        '''
        for poi in self.__getPoints__():
            p = self. __getPixel__(poi[0], poi[1])
            color = fire if poi[2] else noFire
            self.__mark__(offset, p, color)
            
        return self.mapImage
        
        
        
#%% example usage

# =============================================================================
# from skimage import io
# import pandas as pd
# from util.marker import Marker
# 
# img = io.imread('data/2019-12-19/SWIR.tiff')
# validation = pd.read_excel('data/2019-12-19/validation.xlsx')
# bottomLeft = (23.623, 86.148)
# 
# # creating object
# marker = Marker(img, validation, bottomLeft)
# 
# # mraking
# marked = marker.mark(100, (255, 0, 0), (255, 255, 0))
# io.imshow(marked)
# =============================================================================
