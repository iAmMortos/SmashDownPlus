class Player(object):
  def __init__(self, name):
    self.name = name
    self.cur_char = None
    self.wins = 0

  def win(self):
    self.wins += 1

  def reset_wins(self):
    self.wins = 0
