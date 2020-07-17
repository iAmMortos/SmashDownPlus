import ui

class PlayerCharCard(ui.View):
  
  def __init__(self):
    self._score = 0
    self._player_obj = None
    self._has_adv = False
    
    self.bg_img = None
    self.char_img = None
    self.char_lbl = None
    self.char_lbl_bg = None
    self.player_lbl = None
    self.score_lbl = None
    self.score_status_lbl = None

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
    
    self.score_lbl.text = '0'
    self.flex = 'WHLRTB'

  def init(self, player_obj, score, has_adv):
    self._player_obj = player_obj
    self.character = player_obj.cur_char
    self.score = score
    self.player = player_obj.name
    self.set_adv(has_adv)
    
  @property
  def player(self):
    return self._player_obj.name
  
  @player.setter
  def player(self, player_name):
    self._player_obj.name = player_name
    self.player_lbl.text = player_name
     
  @property
  def character(self):
    return self._player_obj.cur_char
    
  @character.setter
  def character(self, char):
    self._player_obj.cur_char = char
    self.bg_img.image = ui.Image.named('imgs/%s_bg.jpg' % char)
    self.char_img.image = ui.Image.named('imgs/%s_0.png' % char)
    self.char_lbl.text = char
    
  @property
  def score(self):
    return self._score
    
  @score.setter
  def score(self, score):
    self._score = score
    self.score_lbl.text = str(score)
    
  def increment_score(self):
    self.score = self.score + 1
    
  def set_adv(self, has_adv):
    if has_adv:
      self.score_status_lbl.alpha = 1
    else:
      self.score_status_lbl.alpha = 0

  @staticmethod
  def load_view(player_obj, score=0, has_adv=False):
    v = ui.load_view()
    v.init(player_obj, score, has_adv)
    return v

