import skimage

rgb2lab = lambda x: skimage.color.rgb2lab([[x]])[0,0,:]
lab2rgb = lambda x: skimage.color.lab2rgb([[x]])[0,0,:]

import numpy as np
print(lab2rgb(np.array([73.0, -29.494755099535887, 27.01961179621946])))
