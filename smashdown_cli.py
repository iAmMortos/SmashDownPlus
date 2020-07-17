from smashdown import SmashDown


class SmashdownCLI (object):
  
  def __init__(self, sd):
    self.smashdown = sd
  
  def print_match_status(sd):
    ps = self.smashdown.get_player_names()
    pws = self.smashdown.get_player_wins_map()
    print('==========\nRound %s:' % self.smashdown.cur_match_num)
    print('  %s matches left after this one.' % self.smashdown.num_matches_left)
    print('Wins:')
    for p in ps:
      print('  %s: %s' % (p, pws[p]))
  
  def smash(sd):
    self.smashdown.deal_chars()
    running = True
    ps = sd.get_player_names()
    while running:
      print_match_status(sd)
      print('---')
      pcs = sd.get_player_char_map()
      for i,p in enumerate(ps):
        print('  %s) %s: %s' % (i+1, p, pcs[p]))
      print('  ---\n  0) Swap Characters')
      inp = input('\nWho won? ')
      if inp == '0':
        sd.swap_chars()
      elif str.isdigit(inp) and 0 < int(inp) <= len(sd.get_player_names()):
        winner = ps[int(inp) - 1]
        print('  Congratulations, %s' % winner)
        sd.winner(winner)
        if sd.num_matches_left == 0:
          running = False
        else:
          sd.deal_chars()
      elif inp.lower() == 'quit':
        print('Bye bye.')
        running = False   
      
  def do_swap():
    pass
  
  def collect_player_names():
    running = True
    players = []
    while running:
      pn = input('Enter a player name (or blank to end): ')
      if pn != '':
        players.append(pn)
      else:
        running = False
    return players


def main():
  players = collect_player_names()
  running = False
  sd = None
  if len(players) == 0:
    print('I mean... you gotta have *players*.')
  else:
    sd = SmashDown('data/characters.txt', 'data/history.txt', players)
    smash(sd)


if __name__ == '__main__':
  main()

