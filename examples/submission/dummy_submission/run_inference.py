"""
This python script is a dummy example of the inference script that populates output/ folder. For this example, the
loading of the model from the directory /model is not taking place and the output/ folder is populated with arrays
filled with zeros of the same size as the images in the input/ folder.
"""

import os
import numpy as np
import nibabel as nib

if __name__ == '__main__':

    input_folder = '/input'
    output_folder = '/output'

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # Load model from /model folder. Here this part is skipped for simplicity reasons.

    for filename in os.listdir(input_folder):
        if filename.endswith(".nii.gz"):
            img = nib.load(os.path.join(input_folder, filename))
            width, height, queue = img.dataobj.shape
            # create random noise as segmentation
            data = np.round(np.random.uniform(low=0, high=1, size=(width, height, queue))).astype(np.uint8)
            dummy_segmentation = nib.Nifti1Image(data, affine=img.affine)
            nib.save(dummy_segmentation, os.path.join(output_folder, filename))
