import os
import shutil
import random
def match_and_split_datasets(outputfolder, image_folder, label_folder, train_ratio=0.7, test_ratio=0.1, val_ratio=0.2):
    """
    将包含图像文件和标签文件的数据集匹配并随机分配为训练集、测试集和验证集。

    参数：
    - image_folder: 包含原始图像文件的文件夹路径
    - label_folder: 包含标签图像文件的文件夹路径
    - train_ratio: 训练集比例，默认为0.7
    - test_ratio: 测试集比例，默认为0.15
    - val_ratio: 验证集比例，默认为0.15

    返回值：
    - 无，但会在指定的文件夹中创建训练集、测试集和验证集的子文件夹，并将相应的图像文件复制到这些子文件夹中。
    """

    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]
    label_files = [f for f in os.listdir(label_folder) if f.endswith('.png')]
    
    # 确保图像文件和标签文件的数量一致
    assert len(image_files) == len(label_files), "图像文件数量与标签文件数量不一致！"
    
    # 将图像文件列表和标签文件列表按照文件名排序
    #image_files.sort()
    #label_files.sort()
    
    random.seed(42)

    # 创建一个列表
    

    # 使用随机种子进行洗牌
    random.shuffle(image_files)
    

    total_size = len(image_files)
    train_size = int(total_size * train_ratio)
    test_size = int(total_size * test_ratio)

    train_image_dir = os.path.join(outputfolder, 'data/train')
    test_image_dir = os.path.join(outputfolder, 'data/test')
    val_image_dir = os.path.join(outputfolder, 'data/val')
    os.makedirs(train_image_dir, exist_ok=True)
    os.makedirs(test_image_dir, exist_ok=True)
    os.makedirs(val_image_dir, exist_ok=True)
    
    train_label_dir = os.path.join(outputfolder, 'label/train')
    test_label_dir = os.path.join(outputfolder, 'label/test')
    val_label_dir = os.path.join(outputfolder, 'label/val')
    os.makedirs(train_label_dir, exist_ok=True)
    os.makedirs(test_label_dir, exist_ok=True)
    os.makedirs(val_label_dir, exist_ok=True)
    
    # 将图像文件和标签文件复制到相应的子文件夹中
    for i in range(total_size):
        image_file = image_files[i]
        label_file = image_files[i] #data和label的文件名是一样的
        
        if i < train_size:
            shutil.copy(os.path.join(image_folder, image_file), os.path.join(train_image_dir, image_file))
            shutil.copy(os.path.join(label_folder, label_file), os.path.join(train_label_dir, label_file))
        elif i < train_size + test_size:
            shutil.copy(os.path.join(image_folder, image_file), os.path.join(test_image_dir, image_file))
            shutil.copy(os.path.join(label_folder, label_file), os.path.join(test_label_dir, label_file))
        else:
            shutil.copy(os.path.join(image_folder, image_file), os.path.join(val_image_dir, image_file))
            shutil.copy(os.path.join(label_folder, label_file), os.path.join(val_label_dir, label_file))


if __name__ == "__main__":

    # image_folder = "d:\\Master_Thesis\\image-super-resolution-master\\notebooks\\ISR_chr\\data\\kwave\\all_24"
    # label_folder = "d:\\Master_Thesis\\image-super-resolution-master\\notebooks\\ISR_chr\\data\\original\\all_24"
    image_folder = "d:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/all_data/Undersampling_ISR/undersampling_256/"
    label_folder = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/all_data/Undersampling_ISR/nolimit_interpolated1000_resized_whiteBackGround_24_512/'
    outputfolder = 'd:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/all_data/Undersampling_ISR/'

    match_and_split_datasets(outputfolder,image_folder, label_folder)


