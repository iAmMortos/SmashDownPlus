
import ui
from smashdown import SmashDown

class SmashDownUI (ui.View):
	
	def did_load(self):
		self.i1 = self['iv_p1']
		self.i1.content_mode = ui.CONTENT_SCALE_ASPECT_FILL
		
		self.i2 = self['iv_p2']
		self.i2.content_mode = ui.CONTENT_SCALE_ASPECT_FILL
		
		self.n1 = self['lbl_p1']
		self.n2 = self['lbl_p2']
		
		self.btn_swap = self['btn_swap']
		self.btn_swap.action = self.swap
		
		self.btn_p1_win = self['btn_p1_win']
		self.btn_p1_win.action = self.p1_win
		
		self.btn_p2_win = self['btn_p2_win']
		self.btn_p2_win.action = self.p2_win
		
	def init(self, charfile, outfile, players):
		self.p1_name, self.p2_name = players
		self.n1.text = self.p1_name
		self.n2.text = self.p2_name
		
		self.sd = SmashDown(charfile, outfile, players)
		self.sd.deal_chars()
		self.update_images()
		
	def update_images(self):
		chars = self.sd.get_player_char_map()
		c1 = chars[self.p1_name]
		c2 = chars[self.p2_name]
		# print(c1, c2)
		self.i1.image = ui.Image.named('imgs/%s_0.png' % c1)
		self.i2.image = ui.Image.named('imgs/%s_0.png' % c2)
		
		
	def swap(self, sender):
		self.sd.swap_chars(self.p1_name, self.p2_name)
		self.update_images()
		
	def p1_win(self, sender):
		self.sd.winner(self.p1_name)
		self.sd.deal_chars()
		self.update_images()
		
	def p2_win(self, sender):
		self.sd.winner(self.p2_name)
		self.sd.deal_chars()
		self.update_images()
	
	@staticmethod
	def load_view(charfile, outfile, players):
		v = ui.load_view()
		v.init(charfile, outfile, players)
		return v
		

if __name__ == '__main__':
	v = SmashDownUI.load_view('characters.txt', 'history_temp.txt', ['Father1337', 'Valfor'])
	v.present(orientations=['landscape'], hide_title_bar=True)
