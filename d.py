import cv2
import numpy as np
from skimage.measure import label, regionprops
import matplotlib.pyplot as plt

def analyze_droplets(image_path):
   
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # print(binary.shape)

    binary = binary[195:265, 285:355]
    
    labeled = label(binary)

    properties = regionprops(labeled)

    min_size = 1  
    max_size = 150

    droplet_sizes = [prop.area for prop in properties if min_size <= prop.area <= max_size]

    valid_labels = [prop.label for prop in properties if min_size <= prop.area <= max_size]

    for region in properties:
        if region.label not in valid_labels:
            labeled[labeled == region.label] = 0


    # print(f"Number of droplets detected: {len(droplet_sizes)}")
    # print("Sizes of droplets (in pixels):", droplet_sizes)


    plt.figure(figsize=(8, 6))
    plt.imshow(labeled, cmap='nipy_spectral')
    plt.title("Detected Droplets")
    plt.axis("off")
    plt.savefig("Final_output.png")

    droplet_sizes.sort()

    with open("data.txt", "w") as file:
        for size in droplet_sizes:
            file.write(f"{size}\n")

    
    return droplet_sizes


image_path = "output.png"
analyze_droplets(image_path)
