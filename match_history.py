from match_result import MatchResult
from datetime import datetime


class MatchHistory(object):
  def __init__(self, historyfile):
    open(historyfile, 'a').close()
    self.historyfile = historyfile
    self.match_results = self._loadresults()

  def add_winner(self, player_dict, winner, timestamp):
    result = MatchResult(player_dict, winner, int(datetime.utcnow().timestamp()))
    self.match_results.append(result)
    with open(self.historyfile, 'a') as f:
      f.write('%s\n' % result)

  def get_win_record(self, count_fn, win_fn):
    total = 0
    won = 0
    for r in self.match_results:
      if count_fn(r):
        total += 1
        if win_fn(r):
          won += 1
    return 0 if total == 0 else won / total

  def get_player_win_record(self, player):
    c = lambda r: r.has_player(player)
    w = lambda r: player == r.winner
    return self.get_win_record(c, w)

  def get_player_win_record_against_player(self, player, other):
    if player == other:
      raise Exception("Player and other must be different.")
    c = lambda r: r.has_players(player, other)
    w = lambda r: player == r.winner
    return self.get_win_record(c, w)

  def get_player_win_record_against_char(self, player, character):
    pass

  def get_player_win_record_against_char_with_char(self, player, char, opchar):
    pass

  def get_player_win_record_with_char_against_opponent_with_character(self, player, char, op, opchar):
    pass

  def get_char_win_record(self, character):
    c = lambda r: character in r.characters
    w = lambda r: r.players[r.winner] == character
    return self.get_win_record(c, w)

  def get_player_win_record_with_char(self, player, character):
    c = lambda r: r.has_player_with_character(player, character)
    w = lambda r: player == r.winner
    return self.get_win_record(c, w)

  def _loadresults(self):
    results = []
    with open(self.historyfile) as f:
      history = f.read()
      for result in history.split('\n'):
        if result.strip() != '':
          results.append(MatchResult.value_of(result))
    return results
