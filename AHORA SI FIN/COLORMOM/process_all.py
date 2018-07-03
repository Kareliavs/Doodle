import os
import numpy as np
import sys
from PIL import Image
from math import floor
import PIL.ImageOps

number_images = 1000; # Number of images in each category
npy_dir = './raw/'
out_dir = './out/'
npy_files = [f for f in os.listdir(npy_dir) if os.path.isfile(os.path.join(npy_dir, f))]
print(npy_files)

categories = []

for x in npy_files:
	category_split = x.split('.')
	category = category_split[0].title()
	categories.append(category)
	
print(categories)

for y in categories:
	if not os.path.exists(os.path.join(out_dir, y)):
		os.makedirs(os.path.join(out_dir, y))

index_cat = 0		
for z in npy_files:
	print('Processing file', z)
	images = np.load(os.path.join(npy_dir, z))
	print('Saving in', categories[index_cat])
	number_imgs = range(0, number_images, 1)
	for a in number_imgs:
		print('Processing Image', a+1)
		file_name = '%s.png' % (a+1)
		file_path = os.path.join(out_dir, categories[index_cat], file_name)
		img = images[a].reshape(28,28)
		f_img = Image.fromarray(img)
		inverted_image = PIL.ImageOps.invert(f_img)
		img2 = inverted_image.convert("RGBA")
		datas = img2.getdata()
		newData = []
		i=0
		c1=c2=c3=c4=c5=c6=c7=c8=c9=0	
		for item in datas:
			#print(i%28+1,floor(i/28+1))
			x=i%28+1
			y=floor(i/28+1)
			if item[0] == 255 and item[1] == 255 and item[2] == 255:
				newData.append((255, 255, 255, 0)) #transparentes
			else:
				#newData.append((0,0,0,255))
				if x<=9 and y<=9: 
					c1=c1+1
				elif x>9 and x<=18 and y<=9: 
					c2=c2+1
				elif x>18 and y<=9: 
					c3=c3+1         ######Cuadrantes superiores
				elif x<=9 and y>9 and y<=18: 
					c4=c4+1
				elif x>9 and x<=18 and y>9 and y<=18: 
					c5=c5+1
				elif x>18 and y>9 and y<=18: 
					c6=c6+1
				elif x<=9 and y>18: 
					c7=c7+1
				elif x>9 and x<=18 and y>18: 
					c8=c8+1
				else: 
					c9=c9+1
				newData.append(item)				
			i=i+1	
		print(c1, c2, c3, c4, c5, c6, c7, c8, c9)
		img2.putdata(newData)
		img2.save(file_path, 'PNG')
	index_cat = index_cat + 1
