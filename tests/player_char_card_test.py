
import test_context
import ui

from views.player_char_card import PlayerCharCard

if __name__ == '__main__':
  from characters import Characters
  from player import Player
  
  import random
  v = ui.View()
  _,_,w,h = v.frame
  cs = Characters().list_alpha()
  names = ['Father1337', 'Valfor']
  players = []
  for i,name in enumerate(names):
    char = random.choice(cs)
    cs.remove(char)
    p = Player(name, i, char)
    players.append(p)
    
  cards = []
  for i,player in enumerate(players):
    card = PlayerCharCard.load_view(player)
    card.flex = 'WHLRTB'
    card.frame = (i*(w/len(players)), 0, w/len(players), h)
    v.add_subview(card)
  v.present(orientations=['landscape'], hide_title_bar=True)

