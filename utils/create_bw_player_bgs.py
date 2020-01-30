
from PIL import Image
import os
import sys
sys.path.append('..')
from characters import Characters


def main():
  os.chdir('..')
  chars = Characters().list_alpha()
  for i, char in enumerate(chars):
    print("Converting %s of %s..." % (i+1, len(chars)))
    imgsrc = 'imgs/%s_bg.jpg' % char
    imgdest = 'imgs/%s_bwbg.jpg' % char
    if not os.path.exists(imgdest):
      Image.open(imgsrc).convert('L').save(imgdest)
  print("Done.")


if __name__ == '__main__':
  main()
