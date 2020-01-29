
import os
from PIL import Image, ImageChops


def main():
  os.chdir('..')
  img1 = Image.open('imgs/Mario_bwbg.jpg').convert('RGB')
  img2 = Image.new('RGB', img1.size, (100, 200, 0))
  ImageChops.multiply(img1, img2).show()


if __name__ == '__main__':
  main()
