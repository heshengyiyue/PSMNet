import os

left_img_path = '/mnt/c/users/public/images/rectified_laparoscope/rectified_left'
right_img_path = '/mnt/c/users/public/images/rectified_laparoscope/rectified_right'

left_img_list = os.listdir(left_img_path)
right_img_list = os.listdir(right_img_path)

for iter in len(left_img_list)
    left_img_filename = left_img_list[iter]
    right_img_filename = right_img_list[iter]
    ml =  'python Test_img.py --loadmodel ./models/pretrained_model_KITTI2015.tar --leftimg '\
          + left_img_filename + ' --rightimg ' + right_img_filename
    os.system(ml)