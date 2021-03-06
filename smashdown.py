import random
from datetime import datetime

from characters import Characters
from match_history import MatchHistory
from player import Player

import sharedlibs
sharedlibs.add_path_for('config_file')
from config_file import ConfigFile
# from smashdown_progress import SmashDownProgress

class SmashDown(object):
  def __init__(self, players=None):
    self.config = ConfigFile('data/app.config')
    self._chars_obj = Characters(self.config.get('characters'))
    self._history = MatchHistory(self.config.get('history'))

    # if type(charfile) == SmashDownProgress:
    #   self.progress = charfile
    #   self.players = self._make_player_dict(self.progress.players)
    #   for i, player in self.players:
    #     self.players[i].wins = self.progress.wins[i]
    #     self.players[i].cur_char = self.progress.current_chars[i]
    #   self.characters = self.progress.remaining_chars
    #   self.total_matches = self.progress.total_matches
    #   self._completed_matches = self.total_matches - (
    #         len(self.progress.remaining_chars) + len(self.progress.current_chars)) // 2
    # else:
    # if players is None:
    #   raise Exception('Argument Exception: the players argument is only optional in the progress constructor.')
    # self.progress = SmashDownProgress()
    self.players = self._make_player_dict(players)
    self.characters = self._chars_obj.list_alpha()
    self.total_matches = len(self.characters) // len(self.players)
    self._completed_matches = 0

    # self.progress.update(self.total_matches, self.players, self.characters)

  def _make_player_dict(self, players):
    p = {}
    for i, player in enumerate(players):
      p[player] = Player(player, i + 1)
    return p

  def deal_chars(self):
    names = {}
    for name in self.players.keys():
      c = random.choice(self.characters)
      names[name] = c
      self.players[name].cur_char = c
      self.characters.remove(c)
    return names

  def reset(self):
    self.characters = self._chars_obj.list_alpha()
    for player in self.players:
      self.players[player].reset_wins()
    self._completed_matches = 0
    self.total_matches = len(self.characters) // len(self.players)
    # self.progress.update(self.total_matches, self.players, self.characters)

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
    self._history.add_winner(self.get_player_char_map(), player, int(datetime.utcnow().timestamp()))
    self._completed_matches += 1
    # if self._completed_matches == self.total_matches:
    #  self.progress.reset()

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

  @property
  def completed_matches(self):
    return self._completed_matches


def get_properties():
  props = {}
  with open('data/app.properties') as f:
    lines = [l.strip() for l in f.readlines()]
    for line in lines:
      if line.strip() != '':
        k, v = line.split('=')
        props[k] = v
  return props


def main():
  players = ['Father1337', 'Valfor']
  sd = SmashDown('data/characters.txt', 'data/history_temp.txt', players)
  # props = get_properties()
  config = ConfigFile('data/app.config')
  run_type = config.get('run_type')

  if run_type == 'cli':
    import smashdown_cli
    smashdown_cli.smash(sd)
  elif run_type == 'gui':
    from views.smashdown_ui import SmashDownUI
    v = SmashDownUI.load_view('data/characters.txt', 'data/history_temp.txt', ['Father1337', 'Valfor'])
    v.present(orientations=['landscape'], hide_title_bar=True)


if __name__ == '__main__':
  main()
