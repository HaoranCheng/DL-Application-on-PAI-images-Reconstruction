
from rembg import remove

#待处理的图片路径
input_path = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/all_data/Ilastik_relabeled/Interpolated/test/reconstructed 7_X_130.png'
#处理后存储的图片路径
output_path = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/all_data/Ilastik_relabeled/Interpolated/output.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

import cv2
import numpy as np

# 读取图像
import cv2
import numpy as np

# 读取灰度图像
gray_image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

# 创建背景移除器
bg_remover = cv2.createBackgroundSubtractorMOG2()

# 进行图像分割
mask = bg_remover.apply(gray_image)

# 对掩码进行形态学操作，去除噪声
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# 创建白色背景图像
white_background = np.ones_like(gray_image) * 255

# 将掩码应用到原始图像上，去除背景并填充为白色
result = cv2.bitwise_or(white_background, gray_image, mask=mask)

# 显示结果图像
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
