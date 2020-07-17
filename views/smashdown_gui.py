
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
    self.info = None
    self.btn_swap = None
    self.btn_p1_win = None
    self.btn_p2_win = None
    self.btn_reset = None
    self.game_over = None

  def did_load(self):
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

