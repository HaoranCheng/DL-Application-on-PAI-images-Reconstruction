import os
import cv2

# Define input and output folders
input_folder = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/100_70/47_kwave_100_recon/'
output_folder = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/100_70/47_kwave_100_recon_24/'

# Ensure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get list of image files in input folder
image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

# Loop through each image file
for image_file in image_files:
    # Read the image
    image_path = os.path.join(input_folder, image_file)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    # Convert image to 24-bit depth (grayscale to BGR)
    img_24bit = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    
    # Save the converted image to output folder
    output_path = os.path.join(output_folder, image_file)
    cv2.imwrite(output_path, img_24bit)

print("Conversion complete.")
