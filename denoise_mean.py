import cv2

# 读取图像
image = cv2.imread('d:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/all_data/Ilastik_relabeled/nolimit_interpolated1000_resized_whiteBackGround/reconstructed 7_X_130.png')

# 将图像转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用中值滤波器去除不清晰线条
#filtered_image = cv2.medianBlur(gray_image, 9)  # 参数5表示中值滤波器的卷积核大小
filtered_image = cv2.fastNlMeansDenoising(gray_image, None, 15, 7, 21)
gaussian = cv2.GaussianBlur(gray_image, (3,3), 0)

# 显示原始图像和处理后的图像
# cv2.imshow('Original Image', gray_image)
# cv2.imshow('Filtered Image', filtered_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import numpy as np
kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])

# 锐化处理
sharpened_image = cv2.filter2D(filtered_image, -1, kernel)
gaussian_sharpened = cv2.filter2D(gaussian, -1, kernel)
#sharpened_image = cv2.

blur_laplace = cv2.Laplacian(image, -1)
dst_laplacian = cv2.addWeighted(image, 1, blur_laplace, -0.5, 0)

denoised_laplace = cv2.Laplacian(filtered_image, -1)
cv2.imshow("denoised + dst_laplace", denoised_laplace)
cv2.imshow("dst_laplacian", dst_laplacian)
# 显示原始图像、去噪后的图像和锐化后的图像
cv2.imshow('Original Image', image)
cv2.imshow('fastNlMeansDenoising Image', filtered_image)
cv2.imshow('gaussian Image', gaussian)
cv2.imshow('fastNlMeansDenoising + Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()