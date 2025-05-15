import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def rmse2(img1, img2):
    return np.sqrt(np.mean((img1 - img2) ** 2))

def calculate_rmse(image1, image2):
    # 如果图像不是灰度图像，则转换为灰度图像
    if len(image1.shape) > 2:
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    if len(image2.shape) > 2:
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
    # 计算差的平方
    diff = (image1.astype(np.float32) - image2.astype(np.float32)) ** 2
    
    # 计算平均差的平方
    mean_squared_diff = np.mean(diff)
    
    # 计算 RMSE
    rmse = np.sqrt(mean_squared_diff)
    
    return rmse
# 加载两张图片
image1 = cv2.imread('d:\\Master_Thesis\\NumerialBreastPhantoms\\hdf5/phan pre post/ISR_result/reconstructed X_351.png')
image1 = cv2.imread('d:\\Master_Thesis\\NumerialBreastPhantoms\\hdf5/phan pre post/ISR_result/X_351.png')
image2 = cv2.imread("d:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/output.png")
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# 计算两张图片的 RMSE
rmse = calculate_rmse(image1, image2)
print("RMSE between the two images:", rmse, rmse2  (image1, image2))

    
