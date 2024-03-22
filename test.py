import os
import nibabel as nib

# Set the path to the folder containing the .nii files
folder_path = 'C:/Users/Meruja/Downloads/Testdata/groud-truth'

# Loop through each file in the folder
for file in os.listdir(folder_path):
    # Check if the file has a .nii extension
    if file.endswith('.nii'):
        # Load the file using nibabel
        img = nib.load(os.path.join(folder_path, file))
        # Save the file as a .nii.gz file
        nib.save(img, os.path.join(folder_path, file[:-4] + '.nii.gz'))