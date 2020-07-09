import views

import sharedlibs
sharedlibs.add_path_for('touch_view')
from touch_view import TouchView

class CharPickerTile (views.View):

  def __init__(self):
    self.callbackfn = lambda s: None
    self.action = lambda s: self.callback()

  def did_load(self):
    self.iv = self['iv']
    self.content_mode = views.CONTENT_SCALE_ASPECT_FIT

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
    self.iv.image = views.Image.named('imgs/%s_thumbh.png' % char)

  def callback(self):
    self.callbackfn(self.char)

  def _reset_border(self):
    self.border_color = '#eee'
    self.border_width = 1
    self.corner_radius = 3

  @staticmethod
  def load_view(char, bg_color='#000'):
    v = views.load_view()
    v.init(char, bg_color)
    return v


if __name__ == '__main__':
  cpt = CharPickerTile.load_view('R.O.B.')
  cpt.frame = (10, 10, 194, 46)
  cpt.action = lambda s: print(cpt.char)
  v = views.View()
  v.add_subview(cpt)
  v.present()
