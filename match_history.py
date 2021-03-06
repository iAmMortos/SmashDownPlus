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
      
  def get_players_list(self):
    players = []
    for result in self.match_results:
      ps = result.players
      for p in ps:
        if p not in players:
          players.append(p)
    return players
    
  def get_count(self, count_fn):
    c = 0
    for r in self.match_results:
      if count_fn(r):
        c += 1
    return c

  def get_win_record(self, count_fn, win_fn):
    total = 0
    won = 0
    for r in self.match_results:
      if count_fn(r):
        total += 1
        if win_fn(r):
          won += 1
    return 0 if total == 0 else won / total
    
  def get_player_num_matches(self, player):
    return self.get_count(lambda r: player in r.players)
    
  def get_player_num_matches_won(self, player):
    return self.get_count(lambda r: player == r.winner)

  def get_player_win_record(self, player):
    c = lambda r: r.has_player(player)
    w = lambda r: player == r.winner
    return self.get_win_record(c, w)

  def get_character_win_record(self, character):
    c = lambda r: character in r.characters
    w = lambda r: r.players[r.winner] == character
    return self.get_win_record(c, w)

  def get_character_win_record_against_opponent(self, character, opponent):
    pass

  def get_character_win_record_against_character(self, char, opchar):
    pass

  def get_character_with_record_against_opponent_with_character(self, char, opponent, opchar):
    pass

  def get_player_win_record_against_player(self, player, opponent):
    if player == opponent:
      raise Exception("Player and other must be different.")
    c = lambda r: r.has_players(player, opponent)
    w = lambda r: player == r.winner
    return self.get_win_record(c, w)

  def get_player_win_record_against_char(self, player, character):
    c = lambda r: r.has_player(player) and character in r.get_opponent_characters(player)
    w = lambda r: player == r.winner
    return self.get_win_record(c, w)

  def get_player_win_record_with_char(self, player, character):
    c = lambda r: r.has_player_with_character(player, character)
    w = lambda r: player == r.winner
    return self.get_win_record(c, w)

  def get_player_win_record_with_char_against_char(self, player, char, opchar):
    c = lambda r: r.has_player_with_character(player, char) and opchar in r.get_opponent_characters(player)
    w = lambda r: player == r.winner
    return self.get_win_record(c, w)

  def get_player_win_record_with_char_against_opponent(self, player, char, opponent):
    c = lambda r: r.has_player(player) and r.get_players_character(player) == char and opponent in r.get_opponents(player)
    w = lambda r: player == r.winner
    return self.get_win_record(c, w)

  def get_player_win_record_with_char_against_opponent_with_character(self, player, char, opponent, opchar):
    c = lambda r: r.has_player(player) and r.get_players_character(player) == char and opponent in r.get_opponents(player) and r.get_players_character(opponent) == opchar
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
    

if __name__ == '__main__':
  mh = MatchHistory('data/history.txt')
  players = mh.get_players_list()
  for player in players:
    c = mh.get_player_num_matches(player)
    w = mh.get_player_num_matches_won(player)
    print('{}: {:.2%} ({}/{})'.format(player, w/c, w, c))
