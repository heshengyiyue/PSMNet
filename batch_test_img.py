import os

left_img_path = '/mnt/e/chen/documents/datamanagement/data/202301091507_rectified_images/1/rectified_left'
right_img_path = '/mnt/e/chen/documents/datamanagement/data/202301091507_rectified_images/1/rectified_right'
output_path = '/mnt/e/chen/documents/datamanagement/data/202301091507_rectified_images/1/psmnet_disparity_int16'

left_img_list = os.listdir(left_img_path)
right_img_list = os.listdir(right_img_path)

for iter in range(len(left_img_list)):
    left_img_filename = left_img_list[iter]
    right_img_filename = right_img_list[iter]
    ml =  'python Test_img.py --loadmodel ./models/pretrained_model_KITTI2015.tar --leftimg ' \
          + os.path.join(left_img_path, left_img_filename) + ' --rightimg ' + os.path.join(right_img_path, right_img_filename) \
          + ' --outputpath ' + os.path.join(output_path, left_img_filename)
    os.system(ml)