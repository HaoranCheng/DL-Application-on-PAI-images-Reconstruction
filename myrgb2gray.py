import cv2

def rgb_to_gray(image_path):
    # Read the RGB image
    rgb_image = cv2.imread(image_path)

    # Convert RGB to grayscale
    gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)

    # Save or display the grayscale image
    cv2.imwrite('D:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/output_100epoch_gray.png', gray_image)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Replace 'your_image.jpg' with the path to your RGB image
rgb_to_gray('D:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/output_100epoch.png')
