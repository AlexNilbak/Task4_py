from PIL import Image
import numpy as np

try:  
    if1 = Image.open("InputFile1.jpg")
    if2 = Image.open("InputFile2.jpg")
except FileNotFoundError:  
    print("File not found")
    exit()
if if1.size != if2.size:
    print("Different sizes")
    exit()
if if1.mode != 'RGB' or if2.mode != 'RGB':
    print("Wrong format")
    exit()

arr1 = np.array(if1)
arr2 = np.array(if2)
for i in range(arr1.shape[0]):
    for j in range(arr1.shape[1]):
        b1 = int(arr1[i, j, 0]) + int(arr1[i, j, 1]) + int(arr1[i, j, 2])
        if b1 > 0:
            b2 = int(arr2[i, j, 0]) + int(arr2[i, j, 1]) + int(arr2[i, j, 2])
            arr1[i, j, 0] = arr1[i, j, 0]*b2/b1
            arr1[i, j, 1] = arr1[i, j, 1]*b2/b1
            arr1[i, j, 2] = arr1[i, j, 2]*b2/b1
img = Image.fromarray(arr1, 'RGB')
img.save("OutputFile.jpg")
