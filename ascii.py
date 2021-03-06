from scipy.misc import imread, imsave, imresize
import numpy as np
import matplotlib.pyplot as plt
import re, sys

if len(sys.argv)!=2 or '.' not in sys.argv[1]:
	print('Usage\n\t'+sys.argv[0]+' <image-file>')
	exit(0)

WIDTH = 124

def get_ascii(p):
	p = 255 - p
	if p<=12:
		return ' '
	if p<=50:
		return '.'
	if p<=75:
		return '*'
	if p<=100:
		return '='
	if p<=125:
		return '|'
	if p<=150:
		return 'J'
	if p<=200:
		return 'P'
	return 'B'

def to_grayscale(img):
	if len(img.shape) == 2:
		return img
	g = np.sum(img, axis=2);
	g = g / 3
	return g

img = imread(sys.argv[1])
h = len(img)
w = len(img[0])
ar = float(h)/w
img = imresize(img, (int(ar*WIDTH/1.75), WIDTH))

img = to_grayscale(img)

print(img)
print(img.shape)

filename = sys.argv[1]
filename = re.sub(r'[.*\.](.*)', '.txt', filename)
file = open(filename, 'w')

for i in range(len(img)):
	ascii_str = ''
	for j in range(len(img[0])):
		ascii_str = ascii_str + get_ascii(img[i][j])
	ascii_str = ascii_str + '\n'
	file.write(ascii_str)

print("Ascii image saved to "+filename)