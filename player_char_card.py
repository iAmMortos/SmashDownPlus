import ui

class PlayerCharCard(ui.View):

  def did_load(self):
    self.bg_img = self['bg_img']
    self.bg_img.content_mode = ui.CONTENT_SCALE_ASPECT_FILL
    self.char_img = self['char_img']
    self.char_img.content_mode = ui.CONTENT_SCALE_ASPECT_FILL
    self.char_lbl = self['char_lbl']
    self.char_lbl_bg = self['char_lbl_bg']
    self.player_lbl = self['player_lbl']
    self.score_lbl = self['score_lbl']
    self.score_status_lbl = self['score_status_lbl']

  def init(self, player, char):
    self.set_char(char)
    self.player_lbl.text = player

  def set_char(self, char):
    self.bg_img.image = ui.Image.named('imgs/%s_bg.jpg' % char)
    self.char_img.image = ui.Image.named('imgs/%s_0.png' % char)
    self.char_lbl.text = char

  @staticmethod
  def load_view(player, char):
    v = ui.load_view()
    v.init(player, char)
    return v


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
