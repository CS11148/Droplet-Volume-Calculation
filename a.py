import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import sys

file_n = file_n = sys.argv[1]

image = cv2.imread(file_n, cv2.IMREAD_GRAYSCALE)

a=20

rows, cols = image.shape
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)

crow, ccol = rows // 2, cols // 2

# Keep only high-frequency components by setting low frequencies to 0
mask = np.ones((rows, cols), np.uint8)
r = a 
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0])**2 + (y - center[1])**2 <= r**2
mask[mask_area] = 0
fshift = fshift * mask

f_ishift = np.fft.ifftshift(fshift)
image_back = np.fft.ifft2(f_ishift)
image_back = np.abs(image_back)

image_resized = cv2.resize(image_back, (cols, rows), interpolation=cv2.INTER_LINEAR)

image_resized=image_resized.astype(np.uint8)

out = Image.fromarray(image_resized)

print(file_n)

out.save("output.png")