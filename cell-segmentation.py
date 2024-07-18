import numpy as np
from matplotlib import pyplot as plt
from skimage import io
from skimage import morphology

def do_region_grow(img, x, y):
    if img[x][y] != False:
        img[x][y] = False
        if x < img.shape[0] - 1:
            do_region_grow(img, x+1, y)
        if x != 0:
            do_region_grow(img, x-1, y)
        if y < img.shape[1] - 1:
            do_region_grow(img, x, y+1)
        if y != 0:
            do_region_grow(img, x, y-1)

img = io.imread("./python-celltest.jpg")
mask_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
size = img.shape

# print(size)
# plt.imshow(img)
# plt.show()

count_cell = 0
for i in range(size[0]):
    for j in range(size[1]):
        color = img[i][j]
        if color[0] > color[1] and color[0] > color[2]:
            mask_img[i][j] = 255

#mask_img = ndimage.binary_erosion(ndimage.binary_dilation(mask_img)).astype(np.int)
mask_img=morphology.remove_small_objects(mask_img, 250)
mask_img=morphology.remove_small_holes(mask_img, 250)

for i in range(size[0]):
    for j in range(size[1]):
        if mask_img[i][j] == True:
            count_cell += 1
            do_region_grow(mask_img, i, j)

print("You found " + str(count_cell) + " regions!")
plt.imshow(mask_img, cmap="grey")
plt.show()


