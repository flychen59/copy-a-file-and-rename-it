# -*-coding:utf-8 -*-

#导入数据包
import  shutil

#导入文件路径
save_path='/home/flychen/frustum-pointnets-master/dataset/KITTI/object/testing/calib'
file_path='/home/flychen/frustum-pointnets-master/dataset/KITTI/object/testing/calib/000000.txt'

#创建复制后的文件名并复制任意次数
seq=1
for i in range(98):
 to_path = save_path + '/' + "{:06d}".format(seq)+'.txt'
 try:
     shutil.copy(file_path,to_path)
 except  shutil.SameFileError:
     pass
 seq+=1







