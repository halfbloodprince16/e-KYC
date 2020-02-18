from PIL import Image
import os, sys
import matplotlib.pyplot as plt

path = "ID_Images"
dirs = os.listdir( path )

def resize():
    for item in dirs:
    	print(item)
    	pos_neg = os.listdir(path+'/'+item+'/')
    	for i in pos_neg:
    		classes = os.listdir(path+'/'+item+'/'+i+'/')
    		for x in classes:
    			print(path+'/'+item+'/'+i+'/'+x)
		        if os.path.isfile(path+'/'+item+'/'+i+'/'+x):
		            im = Image.open(path+'/'+item+'/'+i+'/'+x)
		            plt.imshow(im)
		            plt.plot()
		            f, e = os.path.splitext(path+'/'+item+'/'+i+'/'+x)
		            imResize = im.resize((720,720), Image.ANTIALIAS)
		            
		            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()