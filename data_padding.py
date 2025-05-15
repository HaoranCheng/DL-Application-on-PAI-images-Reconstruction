from PIL import Image

def resize_with_padding(image_path, target_size):
    img = Image.open(image_path)
    new_img = Image.new("RGB", target_size, (128, 128, 128))  # black填充
    #灰色为(128, 128, 128)
    new_img.paste(img, ((target_size[0] - img.width) // 2, (target_size[1] - img.height) // 2))
    return new_img
path = 'D:/Master_Thesis/NumerialBreastPhantoms/data_resize/'
path =  'D:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/kwave/'

import os
#284 411 722
for folder in os.listdir(path):
    for file in os.listdir(path + folder):
        if file.endswith(".png"):
            image = resize_with_padding(path+folder+'/'+file, (256, 256))
            #if not os.path.exists('D:/Master_Thesis/NumerialBreastPhantoms/data_resized/'+ folder):
                #os.makedirs('D:/Master_Thesis/NumerialBreastPhantoms/data_resized/'+ folder)
            if not os.path.exists('D:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/final_data/data_resized/'+folder):
                os.makedirs('D:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/final_data/data_resized/'+folder)
            #image.save('D:/Master_Thesis/NumerialBreastPhantoms/data_resized/'+folder+'/'+ file)
            image.save('D:/Master_Thesis/image-super-resolution-master/notebooks/ISR_chr/data/final_data/data_resized/'+folder+'/'+ file)