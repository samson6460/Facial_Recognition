
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from os import listdir
from os.path import isfile, isdir, join
import os
from os import walk
import glob
import cv2
import numpy as np


     
class process:

    def rename(self,name):
        
        Rename_Path='./Agu_images/'+name+'/'
        f = os.listdir(Rename_Path)
        # print(f)
        print(len(f))
        n = 0
        numb=0
        i = 0
        if os.path.isdir(Rename_Path):
            print("檔案存在。")
        else:
            os.makedirs(Rename_Path)
            print("檔案建立。")


        for i in f:
        # 設定舊檔名（就是路徑+檔名）
            oldname = f[n]

        # 設定新檔名
            newname = name+str(numb) + '.jpg'
        # 用os模組中的rename方法對檔案改名
            os.rename(Rename_Path+oldname, Rename_Path+newname)

            print(oldname, '======>', newname)
            n += 1
            numb+=1

    def Agumentation(self,name):
        Agumentation_path='Agu_images/'+name
        original_path='dataset/'+name
        if os.path.isdir(Agumentation_path):
            print("檔案存在。")
        else:
            os.makedirs(Agumentation_path)
            print("檔案建立。")

        datagen = ImageDataGenerator(
            rotation_range=30.0,
            width_shift_range=5.0,
            height_shift_range=0.0,
            shear_range=0.0,
            zoom_range=0,
            horizontal_flip=True,
            fill_mode='nearest')

        # print(path)
        # print (glob.glob(os.path.join(path,'*.jpg')))
        for root, dirs, file_all in walk(original_path):
            print(root)
            for filename in file_all:
                img_path=root+'/'+filename
                print(" img_path=",img_path )

                img = load_img(img_path)
                
                x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
                
                x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)
                i = 0
            
                for batch in datagen.flow(x, 
                            batch_size=1,
                            save_to_dir='Agu_images/'+name,  
                            save_prefix=filename, 
                            save_format='jpg'):
                    i += 1
                    if i > 20:
                        break  # otherwise the generator would loop indefinitely
            



new_user_name='wen'
_process=process()
_process.Agumentation(new_user_name)
_process.rename(new_user_name)