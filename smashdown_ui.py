
import sharedlibs
sharedlibs.add_path_for('img_utils')
import img_utils

import ui
from PIL import Image
from smashdown import SmashDown

class SmashDownUI (ui.View):
	
	def did_load(self):
		self.i1 = self['iv_p1']
		self.i1.content_mode = ui.CONTENT_SCALE_ASPECT_FIT
		
		self.i2 = self['iv_p2']
		self.i2.content_mode = ui.CONTENT_SCALE_ASPECT_FIT
		
		self.bg1 = self['bg1']
		self.bg1.content_mode = ui.CONTENT_SCALE_ASPECT_FILL
		
		self.bg2 = self['bg2']
		self.bg2.content_mode = ui.CONTENT_SCALE_ASPECT_FILL
		
		self.n1 = self['lbl_p1']
		self.n2 = self['lbl_p2']
		self.c1 = self['ch1']
		self.c2 = self['ch2']
		self.score1 = self['score1']
		self.score2 = self['score2']
		self.adv1 = self['adv1']
		self.adv2 = self['adv2']
		self.info = self['info_lbl']
		
		self.btn_swap = self['btn_swap']
		self.btn_swap.action = self.swap
		
		self.btn_p1_win = self['btn_p1_win']
		self.btn_p1_win.action = self.p1_win
		
		self.btn_p2_win = self['btn_p2_win']
		self.btn_p2_win.action = self.p2_win
		
		self.btn_reset = self['btn_reset']
		self.btn_reset.hidden = True
		self.btn_reset.action = self.reset
		
		self.game_over = False
		
	def init(self, charfile, outfile, players):
		self.p1_name, self.p2_name = players
		self.n1.text = self.p1_name
		self.n2.text = self.p2_name
		
		self.sd = SmashDown(charfile, outfile, players)
		self.sd.deal_chars()
		self.update_display()
		
	def update_display(self):
		chars = self.sd.get_player_char_map()
		wins = self.sd.get_player_wins_map()
		c1 = chars[self.p1_name]
		c2 = chars[self.p2_name]
		self.c1.text = c1
		self.c2.text = c2
		self.i1.image = ui.Image.named('imgs/%s_0.png' % c1)
		self.i2.image = ui.Image.named('imgs/%s_0.png' % c2)
		#bgi1 = Image.open('imgs/%s_bg.jpg' % c1).crop([0,0,960,1080])
		#self.bg1.image = img_utils.pil2ui(bgi1)
		#bgi2 = Image.open('imgs/%s_bg.jpg' % c2).crop([0,0,960,1080])
		#self.bg2.image = img_utils.pil2ui(bgi2)
		self.bg1.image = ui.Image.named('imgs/%s_bg.jpg' % c1)
		self.bg2.image = ui.Image.named('imgs/%s_bg.jpg' % c2)
		
		self.score1.text = str(wins[self.p1_name])
		self.score2.text = str(wins[self.p2_name])
		
		self.adv1.text = ''
		self.adv2.text = ''
		p1w = wins[self.p1_name]
		p2w = wins[self.p2_name]
		ml = self.sd.num_matches_left
		if p1w == p2w and ml == 0:
			self.adv1.text = 'tie!'
			self.adv2.text = 'tie!'
		elif p1w - p2w > ml + 1:
			self.adv1.text = 'win!'
			self.adv2.text = 'lose!'
		elif p1w - p2w + 1 > ml:
			self.adv1.text = '(adv)'
		elif p2w - p1w > ml + 1:
			self.adv2.text = 'win!'
			self.adv1.text = 'lose!'
		elif p2w - p1w + 1 > ml:
			self.adv2.text = '(adv)'
		
		if self.game_over:
			self.btn_reset.hidden = False
			self.btn_p1_win.hidden = True
			self.btn_p2_win.hidden = True
			self.btn_swap.hidden = True
			infotext = 'Game Over! '
			if p1w > p2w:
				infotext += '%s Wins!' % self.p1_name
			elif p1w < p2w:
				infotext += '%s Wins!' % self.p2_name
			else:
				infotext += "It's a tie!"
			self.info.text = infotext
		else:
			self.btn_reset.hidden = True
			self.btn_p1_win.hidden = False
			self.btn_p2_win.hidden = False
			self.btn_swap.hidden = False
			infotxt = 'Round %s of %s. %s matches left after this one.' % (self.sd.cur_match_num, self.sd.total_matches, self.sd.num_matches_left)
			self.info.text = infotxt
		
	def swap(self, sender):
		if not self.game_over:
			self.sd.swap_chars(self.p1_name, self.p2_name)
		self.update_display()
		
	def reset(self, sender):
		self.sd.reset_chars()
		self.sd.reset_wins()
		self.sd.deal_chars()
		self.game_over = False
		self.update_display()
		
	def p1_win(self, sender):
		if not self.game_over:
			self.sd.winner(self.p1_name)
			if self.sd.num_matches_left > 0:
				self.sd.deal_chars()
			else:
				self.game_over = True
			self.update_display()
		
	def p2_win(self, sender):
		if not self.game_over:
			self.sd.winner(self.p2_name)
			if self.sd.num_matches_left > 0:
				self.sd.deal_chars()
			else:
				self.game_over = True
			self.update_display()
	
	@staticmethod
	def load_view(charfile, outfile, players):
		v = ui.load_view()
		v.init(charfile, outfile, players)
		return v
		

if __name__ == '__main__':
	v = SmashDownUI.load_view('characters.txt', 'history_temp.txt', ['Father1337', 'Valfor'])
	v.present(orientations=['landscape'], hide_title_bar=True)
