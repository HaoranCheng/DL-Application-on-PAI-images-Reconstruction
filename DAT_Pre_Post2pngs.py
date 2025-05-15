import os
import numpy as np
import matplotlib.pyplot as plt

#depth, height, width
#07-------------(719, 485, 616)   
#35-------------(722,411,284)
#47-------------(752,615,495)
filename = 'Neg_35_Left'
fileshape = (722,411,284)


pre_data_path = 'D:/Master_Thesis/NumerialBreastPhantoms/'+ filename + '/PreData_Interp.DAT'
post_data_path = 'D:/Master_Thesis/NumerialBreastPhantoms/'+ filename + '/PostData_Interp.DAT'

# Define the output directory for coordinate folders
output_directory_pre = 'D:/Master_Thesis/NumerialBreastPhantoms/'+ filename + '/PreData_Interp'
output_directory_post = 'D:/Master_Thesis/NumerialBreastPhantoms/'+ filename + '/PostData_Interp'

# Create the output directories if they don't exist
os.makedirs(output_directory_pre, exist_ok=True)
os.makedirs(output_directory_post, exist_ok=True)

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

        output_path = os.path.join(output_folder, f"{axis_name}_{i}'.{data_type}")  # Adjust the file format if needed
        # Normalize the data to 0-255 range for image saving
        slice_data_normalized = ((slice_data - np.min(slice_data)) / (np.max(slice_data) - np.min(slice_data))) * 255
        
        slice_data_uint8 = slice_data_normalized.astype(np.uint8)
        #slice_data_uint8 = slice_data.astype(np.uint8)
        plt.imsave(output_path, slice_data_uint8, cmap='gray')

# Load binary data files for pre and post data
pre_data = np.fromfile(pre_data_path, dtype=np.float32).reshape(fileshape)
post_data = np.fromfile(post_data_path, dtype=np.float32).reshape(fileshape)


save_slices(pre_data, output_directory_pre, 'X', 'png')
save_slices(pre_data, output_directory_pre, 'Y', 'png')
save_slices(pre_data, output_directory_pre, 'Z', 'png')

save_slices(post_data, output_directory_post, 'X', 'png')
save_slices(post_data, output_directory_post, 'Y', 'png')
save_slices(post_data, output_directory_post, 'Z', 'png')


# save_slices(pre_data, output_directory_pre + '_without_normal', 'X', 'png')
# save_slices(pre_data, output_directory_pre + '_without_normal', 'Y', 'png')
# save_slices(pre_data, output_directory_pre + '_without_normal', 'Z', 'png')

# # Save slices for post-data along the X, Y, and Z axes
# save_slices(post_data, output_directory_post + '_without_normal', 'X', 'png')
# save_slices(post_data, output_directory_post + '_without_normal', 'Y', 'png')
# save_slices(post_data, output_directory_post + '_without_normal', 'Z', 'png')