import numpy as np

def imgShape(s):
	fay = open(s, "r").readlines()
	float(fay.pop(0))
	fay.pop(0)
	fls = []
	for i in fay:
		fls.append(i.split())
	fl_int = []
	for i in fls:
		fl_tmp = []
		for j in i:
			fl_tmp.append(int(j))
		fl_int.append(fl_tmp.copy())

	img = np.array(fl_int)
	return img

def getPos(img):
	ymin = img.shape[0]
	xmin = img.shape[1]

	for y in range(img.shape[0]):
		for x in range(img.shape[1]):
			if(img[y, x] == 1):
				if(y < ymin):
					ymin = y
				if(x < xmin):
					xmin = x
	return [xmin, ymin]

def getBias(img1, img2):
	first = getPos(img1)
	second = getPos(img2)
	x = first[0] - second[0]
	y = first[1] - second[1]
	print("x:" + str(x) + "  y:" + str(y))




file1 = "img/" + input("Input name file №1 (without .txt): ") + ".txt"
open_file1 = open(file1, "r")

file2 = "img/" + input("Input name file №2 (without .txt): ") + ".txt"
open_file2 = open(file2, "r")

im1 = imgShape(file1)
im2 = imgShape(file2)

open_file1.close()
open_file2.close()

getBias(im1, im2)


	