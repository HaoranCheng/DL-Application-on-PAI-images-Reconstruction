import os
import cv2

# # 定义要处理的文件夹路径
# root_dir = 'D:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/final_data/data/'
# # 定义要保存调整大小后图像的文件夹路径
# output_root_dir  = 'D:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/final_data/data_resized/'

root_dir = 'D:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/dataset1000/limited band BW70/interpolated3all/'

output_root_dir  = 'D:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/dataset1000/limited band BW70/interpolated_resized/'

target_size = (256, 256)

# 遍历文件夹中的图片文件

if os.path.isdir(root_dir):
    print(f"Processing images in folder: {root_dir}")
    
    # 定义当前子文件夹下的输出文件夹路径
    # 确保输出文件夹存在，如果不存在则创建它
    os.makedirs(output_root_dir, exist_ok=True)
    
    # 遍历子文件夹中的图片文件
    for filename in os.listdir(root_dir):
        file_path = os.path.join(root_dir, filename)
        if os.path.isfile(file_path):
            # 读取图片
            
            image = cv2.imread(file_path)

            # 调整图片大小
            resized_image = cv2.resize(image, target_size)

            # 构造输出路径
            #output_filename = os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(output_root_dir, filename)

            # 保存调整大小后的图片到对应的输出文件夹中
            cv2.imwrite(output_path, resized_image)

            print(f"Resized image saved: {output_path}")

