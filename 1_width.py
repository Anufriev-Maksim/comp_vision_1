import numpy as np

file= "img/" + input("Input name file (without .txt): ") + ".txt"
openfile = open(file, "r")
fay = openfile.readlines()
w = float(fay.pop(0))
fay.pop(0)
arr_fl = []
for i in fay:
	arr_fl.append(i.split())
flint = []
for i in arr_fl:
	flt = []
	for u in i:
		flt.append(int(u))
	flint.append(flt.copy())
openfile.close()

def widthImg(image, n):
	maxs = 0
	mins = image.shape[1]
	for y in range(image.shape[0]):
		for x in range(image.shape[1]):
			if(image[y, x] == 1):
				if(x > maxs):
					maxs = x
				elif(x < mins):
					mins = x

	return( float(maxs-mins+1) / n); 

image = np.array(flint)
print(widthImg(image, w))
