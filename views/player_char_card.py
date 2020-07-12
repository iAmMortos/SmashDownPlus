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

