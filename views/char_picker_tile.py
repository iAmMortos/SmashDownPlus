import ui

import sharedlibs
sharedlibs.add_path_for('touch_view')
from touch_view import TouchView

class CharPickerTile (ui.View):

  def __init__(self):
    self.callbackfn = lambda s: None
    self.action = lambda s: self.callback()

  def did_load(self):
    self.iv = self['iv']
    self.content_mode = ui.CONTENT_SCALE_ASPECT_FIT

    self.lbl = self['lbl']

    self.tv = TouchView()
    self.tv.frame = self.frame
    self.tv.flex = 'WH'
    self.tv.action = lambda s: self.action(s)
    self.add_subview(self.tv)

  def init(self, char, bg_color):
    self._reset_border()
    self.bg_color = bg_color
    self.char = char
    self.lbl.text = char
    self.iv.image = ui.Image.named('imgs/%s_thumbh.png' % char)

  def callback(self):
    self.callbackfn(self.char)

  def _reset_border(self):
    self.border_color = '#eee'
    self.border_width = 1
    self.corner_radius = 3

  @staticmethod
  def load_view(char, bg_color='#000'):
    v = ui.load_view()
    v.init(char, bg_color)
    return v
    
