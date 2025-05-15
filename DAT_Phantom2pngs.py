import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os
#This file is to extract images from DAT file,从DAT中提取图片

# Mapping of tissue types to UINT8 values
tissue_mapping = { 
    0: 'Background',
    2: 'Fibroglandular Tissue',
    3: 'Fat',
    4: 'Skin',
    5: 'Vessel'
}
depth = 719
height = 485
width = 616


#depth, height, width
#07-------------(719, 485, 616)   
#35-------------(722,411,284)
#47-------------(752,615,495)
filedict={'Neg_07_Left':(719, 485, 616),'Neg_35_Left': (722,411,284),'Neg_47_Left':(752,615,495)}
##########################################################################
filename = 'Neg_47_Left' #Neg_07_Left' #Neg_35_Left' #Neg_47_Left
##########################################################################

fileshape = filedict[filename]
print('current file info: ', filename, fileshape)

file_path = 'D:/Master_Thesis/NumerialBreastPhantoms/' + filename + '/MergedPhantom.DAT'
output_path = 'D:/Master_Thesis/NumerialBreastPhantoms/' + filename + '_MergedPhantom/'


# file_path = 'D:/Master_Thesis/NumerialBreastPhantoms/Neg_07_Left/MergedPhantom.DAT'
# output_path = 'D:/Master_Thesis/NumerialBreastPhantoms/Neg_07_Left/MergedPhantom/'
if not os.path.exists(output_path):
    os.makedirs(output_path)
with open(file_path, 'rb') as file:
    binary_data = np.fromfile(file, dtype=np.uint8)

# Reshape the 1D array into a 3D matrix
matrix_3d = binary_data.reshape(fileshape)

# Iterate through slices and save original grayscale images

def save_slices(data, output_folder, axis_name, data_type):
    # Determine the axis index based on the axis_name
    os.makedirs(output_folder, exist_ok=True)
    axis_index = {'X': 0, 'Y': 1, 'Z': 2}[axis_name]
    
    # Iterate over slices along the specified axis and save them to the output_folder
    for i in range(data.shape[axis_index]):
        # Extract the slice along the specified axis
        if axis_name == 'X':
            slice_data = data[i, :, :]
        elif axis_name == 'Y':
            slice_data = data[:, i, :]
        elif axis_name == 'Z':
            slice_data = data[:, :, i]

        output_path = os.path.join(output_folder, f"{axis_name}_{i}.{data_type}")  # Adjust the file format if needed
        # Normalize the data to 0-255 range for image saving
        #slice_data_normalized = ((slice_data - np.min(slice_data)) / (np.max(slice_data) - np.min(slice_data))) * 255
        
        #slice_data_uint8 = slice_data_normalized.astype(np.uint8)
        slice_data_uint8 = slice_data.astype(np.uint8)
        plt.imsave(output_path, slice_data_uint8, cmap='gray')

save_slices(matrix_3d, output_path, 'X', 'png')
save_slices(matrix_3d, output_path, 'Y', 'png')
save_slices(matrix_3d, output_path, 'Z', 'png')

###############################################
# for i in range(matrix_3d.shape[0]): 
#     current_slice = matrix_3d[i, :, :]

#     plt.imsave(f'{output_path}phan_image_{i}.png', current_slice, cmap='gray')













#import matplotlib.pyplot as plt
#from matplotlib.colors import ListedColormap
# cmap = ListedColormap(['#808080', '#0000FF'])  # Gray for background, Blue for vessel

# # Iterate through slices and save color composite images
# for i in range(matrix_3d.shape[0]):  # Iterate over the depth of the 3D matrix
#     current_slice = matrix_3d[i, :, :]

#     # Create a binary mask for vessel and background
#     vessel_mask = (current_slice == 5)
#     background_mask = (current_slice == 0)

#     # Create a color composite image
#     composite_image = np.zeros_like(current_slice, dtype=np.uint8)
#     composite_image[vessel_mask] = 1  # Set vessel pixels to 1
#     composite_image[background_mask] = 0  # Set background pixels to 0

#     # Save the color composite image
#     plt.imsave(f'{output_path}color_composite_slice_{i}.png', composite_image, cmap=cmap)

