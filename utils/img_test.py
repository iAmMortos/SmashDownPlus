
import os
from PIL import Image, ImageChops
import sharedlibs
sharedlibs.add_path_for('img_utils')
import img_utils


def main():
  os.chdir('..')
  img1 = Image.open('imgs/Mario_bwbg.jpg').convert('RGB')
  img2 = Image.new('RGB', img1.size, (100, 200, 0))
  img_utils.pil2ui(ImageChops.multiply(img1, img2)).show()


if __name__ == '__main__':
  main()
  
