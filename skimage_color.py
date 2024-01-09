import skimage

rgb2lab = lambda x: skimage.color.rgb2lab([[x]])[0,0,:]
lab2rgb = lambda x: skimage.color.lab2rgb([[x]])[0,0,:]

