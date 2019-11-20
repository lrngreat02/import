# image cover to black&white
# pip install pillow

from PIL import image
import os

for file in os.listdir('orig'):  # file 的type 是str
	if file.endswith('.jpg'):
		image_file = Image.open(os.path.join('orig', file)) #open color image
		image_file = image_file.covert('L') # covert image to black&white
		image_file.save(os.path.join('result', file[:4] + '_grey.png'))