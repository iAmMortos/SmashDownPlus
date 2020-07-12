
import test_context
import ui

from views.player_char_card import PlayerCharCard

if __name__ == '__main__':
  from characters import Characters
  
  import random
  v = ui.View()
  _,_,w,h = v.frame
  cs = Characters().list_alpha()
  players = ['Father1337', 'Valfor']
  cards = []
  for i, player in enumerate(players):
    char = random.choice(cs)
    cs.remove(char)
    card = PlayerCharCard.load_view(player, char)
    card.flex = 'WHLRTB'
    card.frame = (i*(w/len(players)), 0, w/len(players), h)
    v.add_subview(card)
  v.present(orientations=['landscape'], hide_title_bar=True)

