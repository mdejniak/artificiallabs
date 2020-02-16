import numpy as np
from PIL import Image
#xor
im1 = Image.open("p5a.bmp")
im2 = Image.open("p5b.bmp")


im1np = np.array(im1)*255
im2np = np.array(im2)*255

result = np.bitwise_xor(im1np, im2np).astype(np.uint8)

Image.fromarray(result).save('result.png')