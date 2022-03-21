
"""
pip install patchify
"""

import numpy as np
from matplotlib import pyplot as plt
from patchify import patchify
import tifffile as tiff

large_image_stack = tiff.imread('E:/tiff_img/128_patches/images_as_128x128_patches.tif')
large_mask_stack = tiff.imread('E:/tiff_img/128_patches/masks_as_128x128_patches.tif')

count1=0
for img in range(large_image_stack.shape[0]):

    large_image = large_image_stack[img]
    
    patches_img = patchify(large_image, (128, 128), step=128)  #Step=128 for 128 patches means no overlap
    
    for i in range(patches_img.shape[0]):
        for j in range(patches_img.shape[1]):
            
            single_patch_img = patches_img[i,j,:,:]
            tiff.imwrite('E:/tiff_img/128_patches/images/' + 'image' + str(count1) + ".tif", single_patch_img)
            count1 = count1+1

count2=0
for msk in range(large_mask_stack.shape[0]):
     
    large_mask = large_mask_stack[msk]
    
    patches_mask = patchify(large_mask, (128, 128), step=128)  #Step=128 for 128 patches means no overlap
    

    for i in range(patches_mask.shape[0]):
        for j in range(patches_mask.shape[1]):
            
            single_patch_mask = patches_mask[i,j,:,:]
            tiff.imwrite('E:/tiff_img/128_patches/masks/' + 'mask' + str(count2) + ".tif", single_patch_mask)
            single_patch_mask = single_patch_mask / 255.
            count2 = count2+1
            


