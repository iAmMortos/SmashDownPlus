import sharedlibs
sharedlibs.add_path_for('img_utils', 'color_utils')
import img_utils
from color_utils import Color

import ui
from PIL import Image
from smashdown import SmashDown
from player import Player

class SmashDownGUI (ui.View):

  def __init__(self):
    self.i1 = None
    self.i2 = None
    self.bg1 = None
    self.bg2 = None
    self.n1 = None
    self.n2 = None
    self.c1 = None
    self.c2 = None
    self.score1 = None
    self.score2 = None
    self.adv1 = None
    self.adv2 = None
    self.info = None
    self.btn_swap = None
    self.btn_p1_win = None
    self.btn_p2_win = None
    self.btn_reset = None
    self.game_over = None

  def did_load(self):
    self.i1 = self['iv_p1']
    self.i1.content_mode = ui.CONTENT_SCALE_ASPECT_FIT

    self.i2 = self['iv_p2']
    self.i2.content_mode = ui.CONTENT_SCALE_ASPECT_FIT

    self.bg1 = self['bg1v']['bg1']
    self.bg1.content_mode = ui.CONTENT_SCALE_ASPECT_FILL

    self.bg2 = self['bg2v']['bg2']
    self.bg2.content_mode = ui.CONTENT_SCALE_ASPECT_FILL

    self.n1 = self['lbl_p1']
    self.n2 = self['lbl_p2']
    self.c1 = self['ch1']
    self.c1.bg_color = Color(0, 0, 0, .2).as_tuple()
    self.c2 = self['ch2']
    self.c2.bg_color = Color(0, 0, 0, .2).as_tuple()
    self.score1 = self['score1']
    self.score2 = self['score2']
    self.adv1 = self['adv1']
    self.adv2 = self['adv2']
    self.info = self['info_lbl']
    self.info.bg_color = Color(0, 0, 0, .5).as_tuple()

    self.btn_swap = self['btn_swap']
    self.btn_swap.action = self.swap
    sbc = Color(self.btn_swap.bg_color)
    sbc.a = .7
    self.btn_swap.bg_color = sbc.as_tuple()

    self.btn_p1_win = self['btn_p1_win']
    self.btn_p1_win.action = self.p1_win
    p1bc = Color(Player.get_color_for_player(1))
    p1bc.a = .7
    self.btn_p1_win.bg_color = p1bc.as_tuple()

    self.btn_p2_win = self['btn_p2_win']
    self.btn_p2_win.action = self.p2_win
    p2bc = Color(Player.get_color_for_player(2))
    p2bc.a = .7
    self.btn_p2_win.bg_color = p2bc.as_tuple()

    self.btn_reset = self['btn_reset']
    rbc = Color(self.btn_reset.bg_color)
    rbc.a = .5
    self.btn_reset.bg_color = rbc.as_tuple()
    self.btn_reset.hidden = True
    self.btn_reset.action = self.reset

    self.game_over = False

