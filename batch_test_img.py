import os

left_img_path = '/mnt/c/users/public/images/rectified_laparoscope/rectified_left'
right_img_path = '/mnt/c/users/public/images/rectified_laparoscope/rectified_right'
#.png Directory(output)
png_path = '/mnt/c/users/public/images/results_png'
length = len(os.listdir(left_img_path))
for flo_file in os.listdir(flo_path):
    flo_file_path = os.path.join(flo_path, flo_file)
    basename, ext = os.path.splitext(flo_file)
    png_file = basename + '.png'
    png_file_path = os.path.join(png_path, png_file)
    ml = './color_flow\t' + flo_file_path + '\t' + png_file_path
    print(ml)
    os.system(ml)