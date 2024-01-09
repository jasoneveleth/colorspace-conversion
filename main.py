import numpy as np
import matplotlib.pyplot as plt

# in the other files
from skimage_color import lab2rgb
from skimage_color import rgb2lab
from tf_color import lab_to_rgb
from tf_color import rgb_to_lab

r = 0x07
g = 0x23
b = 0xD6
blue = np.array([r, g, b], dtype=np.uint8).astype(np.float64)/255
r = 0xFF
g = 0x4B
b = 0x4C
red = np.array([r, g, b], dtype=np.uint8).astype(np.float64)/255

n = 100

print("should be the same:")
print(rgb2lab(blue))
print(rgb_to_lab(blue).numpy())
print("should be the same")
print(blue)
print(lab2rgb(rgb2lab(blue)))
print(lab_to_rgb(rgb_to_lab(blue)).numpy())
print('========================')

def interp(r, b, t):
    return lab2rgb(t*rgb2lab(b) + (1-t)*rgb2lab(r))

def interp2(r, b, t):
    return t*b + (1-t)*r

i = [np.tile(interp(red, blue, (i/(n-1))), (6, 1, 1)) for i in range(n)]
j = [np.tile(interp2(red, blue, (i/(n-1))), (6, 1, 1)) for i in range(n)]
i = np.hstack(i)
j = np.hstack(j)
k = np.ones_like(i)
plt.imshow(np.vstack((i,k,j)))
plt.show()

