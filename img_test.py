
import ui
from PIL import Image, ImageEnhance

uiimg = True
imgpath = 'imgs/Mario_bg.jpg'

def main():
  if uiimg:
    bg = ui.Image.named(imgpath)
    with ui.ImageContext(*bg.size) as ctx:
      bg.draw()
      ctx.get_image().show()
  else:
    bg = Image.open(imgpath)
    cnv = ImageEnhance.Color(bg)
    bgg = cnv.enhance(0)
    bgg.show()


if __name__ == '__main__':
  main()

