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

  def get_win_rate(self, player):
    total = 0
    won = 0
    for r in self.match_results:
      if player in r.players:
        total += 1
      if player == r.winner:
        won += 1
    return 0 if total == 0 else won / total

  def _loadresults(self):
    results = []
    with open(self.historyfile) as f:
      history = f.read()
      for result in history.split('\n'):
        if result.strip() != '':
          results.append(MatchResult.value_of(result))
    return results
