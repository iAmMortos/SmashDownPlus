class MatchResult(object):
  def __init__(self, player_dict, winner, time):
    self.players = player_dict
    self.winner = winner
    self.timestamp = time

  def __repr__(self):
    ps = sorted(list(self.players.keys()))
    wi = ps.index(self.winner)
    return '%s\t%s\t%s' % (self.timestamp, wi, '\t'.join(['%s|%s' % (p, self.players[p]) for p in ps]))

  def get_opponent_characters(self, player):
    characters = []
    for p in self.players:
      if p != player:
        characters.append(self.players[p])
    return characters

  def has_player(self, player):
    return player in self.players

  def has_players(self, *players):
    for p in players:
      if p not in self.players:
        return False
    return True

  def has_character(self, character):
    return character in self.characters

  def has_player_with_character(self, player, character):
    return player in self.players and self.players[player] == character

  @property
  def characters(self):
    return list(self.players.values())

  @staticmethod
  def value_of(st):
    parts = st.split('\t')
    timestamp = int(parts[0])
    winner_idx = int(parts[1])
    winner = ''
    player_strs = parts[2:]
    players = {}
    for i, pstr in enumerate(player_strs):
      player, character = pstr.split('|')
      if i == winner_idx:
        winner = player
      players[player] = character
    return MatchResult(players, winner, timestamp)
