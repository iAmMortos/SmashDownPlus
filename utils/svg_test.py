from cairosvg import svg2png

with open("../imgs/Villager_mark.svg", 'rb') as f:
  svg2png(bytestring=f.read(), write_to="test_mark.png")
