
import os

class SmashDownProgress (object):
  
  def __init__(self, file='data/progress.txt'):
    self.outfile = file
    self.total_matches = 0
    self.players = []
    self.wins = []
    self.current_chars = []
    self.remaining_chars = []
    self.load()
  
  def reset(self):
    self.total_matches = 0
    self.players = []
    self.wins = []
    self.current_chars = []
    self.remaining_chars = []
    self._write()
    
  def _write(self):
    with open(self.outfile, 'w') as f:
      out = []
      out.append(str(self.total_matches))
      out.append('|'.join(self.players))
      out.append('|'.join([str(i) for i in self.wins]))
      out.append('|'.join(self.current_chars))
      out.append('|'.join(self.remaining_chars))
      f.write('\n'.join(out))
    
  def update(self, total_matches, players, remaining_chars):
    self.total_matches = total_matches
    names = [player.name for player in sorted(players.values(), key=lambda p: p.num)]
    self.players = names
    self.wins = [players[n].wins for n in names]
    self.current_chars = [players[n].cur_char for n in names]
    self.remaining_chars = remaining_chars
    self._write()
      
  def load(self):
    if not os.path.exists(self.outfile):
      self._write()
    else:
      with open(self.outfile) as f:
        lines = f.read().split('\n')
        self.total_matches = 0 if lines[0] == '' else int(lines[0])
        self.players = lines[1].split('|')
        self.wins = [] if lines[2] == '' else [int(w) for w in lines[2].split('|')]
        self.current_chars = lines[3].split('|')
        self.remaining_chars = lines[4].split('|')
