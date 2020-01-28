
import ui
import math
from char_picker_tile import CharPickerTile
from characters import Characters

class CharPicker(ui.View):
	def __init__(self):
		self._tile_size = (194, 47)
		self.sort_mode = 'Roster'
		
	def did_load(self):
		self.sv = self['sv']
		self.chars = Characters()
		self.tiles = [CharPickerTile.load_view(ch) for ch in self.chars.list_roster()]
		for tile in self.tiles:
			self.sv.add_subview(tile)
		
	def layout(self):
		w = self.frame[2] // self._tile_size[0]
		hpad = self.frame[2] % self._tile_size[0] / 3
		vpad = 8
		tw, th = self._tile_size
		cxi = 0
		cyi = 0
		for tile in self.tiles:
			tile.frame = ((hpad + tw) * cxi + hpad, (vpad + th) * cyi + vpad, tw, th)
			cxi += 1
			if cxi >= w:
				cyi += 1
				cxi = 0
		self.sv.content_size = (self.frame[2], math.ceil(len(self.chars) / w) * (th + vpad) + vpad)
		
	@staticmethod
	def load_view():
		return ui.load_view()
		
if __name__ == '__main__':
	v = CharPicker.load_view()
	v.present()
