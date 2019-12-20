
import random
from player import Player


class SmashDown (object):
	def __init__(self, charfile, players):
		self.charfile = charfile
		self.players = self._make_player_dict(players)
		self.characters = self._loadchars(charfile)
		self.totalrounds = len(self.characters) // len(self.players)

	def _loadchars(self, file):
		cs = []
		with open(file) as f:
			for line in f.read().split('\n'):
				if line.strip() != '' and not line.startswith('#'):
					cs += [line.strip()]
		return cs
		
	def _make_player_dict(self, players):
		p = {}
		for player in players:
			p[player] = Player(player)
		return p
		
	def deal_chars(self):
		names = {}
		for name in self.players.keys():
			c = random.choice(self.characters)
			names[name] = c
			self.players[name].cur_char = c
			self.characters.remove(c)
		return names
		
	def reset_chars(self):
		self.characters = self._loadchars(self.charfile)
		
	def swap_chars(self, p1=None, p2=None):
		if p1==None and p2==None and self.num_players == 2:
			p1, p2 = self.players.keys()
			
		if p1 not in self.players:
			raise Exception('No player by name [%s].' % p1)
		if p2 not in self.players:
			raise Exception('No player by name [%s].' % p2)
			
		c = self.players[p1].cur_char
		self.players[p1].cur_char = self.players[p2].cur_char
		self.players[p2].cur_char = c
		
	def print_cur_chars(self):
		ps = sorted(self.players.keys())
		for p in ps:
			print('%s: %s' % (p, self.players[p].cur_char))
					
	@property
	def num_players(self):
		return len(self.players)
		
	@property
	def num_characters_left(self):
		return len(self.characters)
		
	@property
	def num_matches_left(self):
		return self.num_characters_left // self.num_players
	

def main():
	sd = SmashDown('characters.txt', ['Father1337', 'Valfor'])
	sd.deal_chars()
	sd.print_cur_chars()
	sd.swap_chars()
	sd.print_cur_chars()
	sd.deal_chars()
	sd.print_cur_chars()

if __name__ == '__main__':
	main()
