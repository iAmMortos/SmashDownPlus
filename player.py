class Player(object):
  def __init__(self, name, num, char=None):
    self.name = name
    self.num = num
    self.color = Player.get_color_for_player(num)
    self.cur_char = char
    self.wins = 0

  def win(self):
    self.wins += 1

  def reset_wins(self):
    self.wins = 0
    
  @staticmethod
  def get_color_for_player(num):
    colors = []
    with open('data/player_colors.txt') as f:
      colors = [a.strip() for a in f.readlines()]
    return colors[num - 1]
