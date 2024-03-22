import os
import shutil

# Set the path to the folder containing the .nii.gz files
source_folder = 'C:/Users/Meruja/Downloads/Testdata/test-nifti'

# Set the path to the new location for the renamed files
target_folder = 'C:/Users/Meruja/Downloads/Testdata/test-rename'

# Create the new folder if it doesn't exist
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Loop through each file in the source folder
for file in os.listdir(source_folder):
    # Check if the file has a .nii.gz extension
    if file.endswith('.nii_000.gz'):
        # Get the file name without the extension
        name = file[:-7]

        # Create the new file name
        new_name = f'{name}_000.nii.gz'

        # Move the file to the new location with the new name
        shutil.move(os.path.join(source_folder, file), os.path.join(target_folder, new_name))