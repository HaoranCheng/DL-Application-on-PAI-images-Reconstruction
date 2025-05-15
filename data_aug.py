import os
import numpy as np
from PIL import Image

# 设置数据路径
data_list = ['train', 'val', 'test']
data_split = data_list[0]

# data_dir = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/final_data/data/' + data_split + '/'
# label_dir = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/final_data/labels/' + data_split + '/'   
# output_data_dir = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/final_data/data_aug/' + data_split + '/'
# output_label_dir = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/final_data/labels_aug/' + data_split + '/'

data_dir = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/all_data/bandlimited/aug/data_resized/' + data_split + '/'
label_dir = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/all_data/bandlimited/aug/label_resized/' + data_split + '/'   
output_data_dir = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/all_data/bandlimited/aug/aug_data/' + data_split + '/'
output_label_dir = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/all_data/bandlimited/aug/aug_label/' + data_split + '/'

if not os.path.exists(output_data_dir):
    os.makedirs(output_data_dir)
if not os.path.exists(output_label_dir):
    os.makedirs(output_label_dir)

# 加载数据和标签
data_filenames = os.listdir(data_dir)
label_filenames = os.listdir(label_dir)

# 确保数据和标签文件名一一对应
data_filenames.sort()
label_filenames.sort()

# 对每个图像进行上下、左右、上下左右翻转并保存
for data_file, label_file in zip(data_filenames, label_filenames):
    # 加载数据和标签图像
    data_img = Image.open(os.path.join(data_dir, data_file))
    label_img = Image.open(os.path.join(label_dir, label_file))
    data_img.save(os.path.join(output_data_dir, 'original_' + data_file))
    label_img.save(os.path.join(output_label_dir, 'original_' + label_file))
    # 上下翻转
    data_flipped_up_down = data_img.transpose(Image.FLIP_TOP_BOTTOM)
    label_flipped_up_down = label_img.transpose(Image.FLIP_TOP_BOTTOM)
    data_flipped_up_down.save(os.path.join(output_data_dir, 'flipped_ud_' + data_file))
    label_flipped_up_down.save(os.path.join(output_label_dir, 'flipped_ud_' + label_file))

    # 左右翻转
    data_flipped_left_right = data_img.transpose(Image.FLIP_LEFT_RIGHT)
    label_flipped_left_right = label_img.transpose(Image.FLIP_LEFT_RIGHT)
    data_flipped_left_right.save(os.path.join(output_data_dir, 'flipped_lr_' + data_file))
    label_flipped_left_right.save(os.path.join(output_label_dir, 'flipped_lr_' + label_file))

    # 上下左右翻转
    data_flipped_both = data_flipped_up_down.transpose(Image.FLIP_LEFT_RIGHT)
    label_flipped_both = label_flipped_up_down.transpose(Image.FLIP_LEFT_RIGHT)
    data_flipped_both.save(os.path.join(output_data_dir, 'flipped_both_' + data_file))
    label_flipped_both.save(os.path.join(output_label_dir, 'flipped_both_' + label_file))
