
import ui
from views.player_char_card import PlayerCharCard

class PlayerCharCardBoard (ui.View):
  def __init__(self, players):
    self.players = players
    self.cards = []
    _,_,w,h = self.frame
    for i,p in enumerate(self.players):
      card = PlayerCharCard.load_view(p)
      card.frame = (i*(w/len(self.players)), 0, w/len(self.players), h)
      self.cards.append(card)
      self.add_subview(card)
