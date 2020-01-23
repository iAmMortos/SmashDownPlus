import random
from player import Player
from match_history import MatchHistory
from datetime import datetime


class SmashDown(object):
  def __init__(self, charfile, outfile, players):
    self.charfile = charfile
    self.outfile = outfile
    self.players = self._make_player_dict(players)
    self.characters = self._loadchars(charfile)
    self.total_matches = len(self.characters) // len(self.players)
    self.history = MatchHistory(self.outfile)

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
    
  def reset_wins(self):
  	for player in self.players:
  		self.players[player].reset_wins()

  def swap_chars(self, p1=None, p2=None):
    if p1 is None and p2 is None and self.num_players == 2:
      p1, p2 = self.players.keys()

    if p1 not in self.players:
      raise Exception('No player by name [%s].' % p1)
    if p2 not in self.players:
      raise Exception('No player by name [%s].' % p2)

    self.players[p1].cur_char, self.players[p2].cur_char = self.players[p2].cur_char, self.players[p1].cur_char

  def print_cur_chars(self):
    ps = sorted(self.players.keys())
    for p in ps:
      print('%s: %s' % (p, self.players[p].cur_char))

  def get_player_char_map(self):
    return {p: self.players[p].cur_char for p in self.players}
    
  def get_player_wins_map(self):
  	return {p: self.players[p].wins for p in self.players}

  def get_player_names(self):
    return sorted(list(self.players.keys()))

  def winner(self, player):
    self.players[player].win()
    self.history.add_winner(self.get_player_char_map(), player, int(datetime.utcnow().timestamp()))

  @property
  def num_players(self):
    return len(self.players)

  @property
  def num_characters_left(self):
    return len(self.characters)

  @property
  def num_matches_left(self):
    return self.num_characters_left // self.num_players
    
  @property
  def cur_match_num(self):
  	return self.total_matches - self.num_matches_left


def main():
  players = ['Father1337', 'Valfor']
  sd = SmashDown('characters.txt', 'history.txt', players)


if __name__ == '__main__':
  main()
