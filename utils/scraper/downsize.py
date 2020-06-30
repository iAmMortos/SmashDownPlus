
from PIL import Image
import os

srcbase = '../../imgs'
destbase = 'imgs_small'

min_size = (960, 1024)

chars = []
with open('nintendo_chars.txt') as f:
	chars = [line.strip().split('\t')[1] for line in f.readlines()]
print(chars)

def get_fit_image_size(min_size, img_size):
	min_w, min_h = min_size
	img_w, img_h = img_size
	if img_w > min_w and img_h > min_h:
		new_w = min_h * img_w // img_h
		new_h = min_w * img_h // img_w
		if new_w < min_w:
			return (min_w, new_h)
		else:
			return (new_w, min_h)
	else:
		print("Image already small enough ({}x{}).".format(img_w, img_h))
		return img_size

for i, char in enumerate(chars):
	print('{} {}/{} - '.format(char, i+1, len(chars)), end='')
	for i in range(8):
		filename = '{}_{}.png'.format(char, i)
		srcfile = '{}/{}'.format(srcbase, filename)
		destfile = '{}/{}'.format(destbase, filename)
		if os.path.exists(srcfile):
			print('{} '.format(i), end='')
			img = Image.open(srcfile)
			new_size = get_fit_image_size(min_size, img.size)
			img.resize(new_size, resample=Image.BICUBIC).save(destfile)
	print()
print("Done.")
