
import ui
import math
from char_picker_tile import CharPickerTile
from characters import Characters

class CharPicker(ui.View):
	def __init__(self):
		self._tile_size = (194, 47)
		self.result = None
		
	def did_load(self):
		self.sv = self['sv']
		self.sc = self['sc']
		self.sc.action = self.handle_seg_change
		
		self.chars = Characters()
		self.tiles = {ch:CharPickerTile.load_view(ch) for ch in self.chars.list_roster()}
		for ch in self.tiles:
			tile = self.tiles[ch]
			tile.callbackfn = self.handle_choose
			self.sv.add_subview(tile)
		
	def layout(self):
		w = self.frame[2] // self._tile_size[0]
		hpad = self.frame[2] % self._tile_size[0] / (w+1)
		vpad = 8
		tw, th = self._tile_size
		cxi = 0
		cyi = 0
		val = self.sc.segments[self.sc.selected_index]
		chs = self.chars.list_roster() if val == 'Roster' else self.chars.list_alpha()
		for ch in chs:
			tile = self.tiles[ch]
			tile.frame = ((hpad + tw) * cxi + hpad, (vpad + th) * cyi + vpad, tw, th)
			cxi += 1
			if cxi >= w:
				cyi += 1
				cxi = 0
		self.sv.content_size = (self.frame[2], math.ceil(len(self.chars) / w) * (th + vpad) + vpad)
		
	def handle_seg_change(self, sender):
		self.layout()
		
	def handle_choose(self, ch):
		self.result = ch
		self.close()
		
	@staticmethod
	def load_view():
		return ui.load_view()
		
if __name__ == '__main__':
	v = CharPicker.load_view()
	v.present()
	v.wait_modal()
	print(v.result)
