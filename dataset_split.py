import os
from util import make_dir 
import shutil

dataset_folder = 'gestures'
gestures_list = os.listdir(dataset_folder)
gestures_list.sort()
print('gesture folder list -->', gestures_list)
print('\n',len(gestures_list) ,'of classes will be split(none class folder skip)')
n_of_valid_set = 100

make_dir(os.path.join(dataset_folder, 'valid'))

for gesture in gestures_list:
	if gesture.isdigit() :
		print('gesture :',gesture, 'is moving')
		dest_path = os.path.join(dataset_folder, 'valid', gesture)
		make_dir(dest_path)
		origin_path = os.path.join(dataset_folder, gesture)
		image_list = os.listdir(origin_path)
		n_of_image = 0
		for image in image_list:
			if n_of_image >= n_of_valid_set:
				break
			shutil.move(os.path.join(origin_path, image), os.path.join(dest_path, image))
			n_of_image += 1
