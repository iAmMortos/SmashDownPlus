class Player (object):
	def __init__(self, name):
		self.name = name
		self.cur_char = None
		self.wins = 0
		
	def count_win(self):
		self.wins += 1
