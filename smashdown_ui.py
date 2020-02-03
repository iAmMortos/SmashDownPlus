
import sharedlibs
sharedlibs.add_path_for('img_utils', 'color_utils')
import img_utils
from color_utils import Color

import ui
from PIL import Image
from smashdown import SmashDown
from smashdown_progress import SmashDownProgress
from player import Player

class SmashDownUI (ui.View):

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
    self.c1.bg_color = Color(0,0,0,.2).as_tuple()
    self.c2 = self['ch2']
    self.c2.bg_color = Color(0,0,0,.2).as_tuple()
    self.score1 = self['score1']
    self.score2 = self['score2']
    self.adv1 = self['adv1']
    self.adv2 = self['adv2']
    self.info = self['info_lbl']
    self.info.bg_color = Color(0,0,0,.5).as_tuple()

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

  def init(self, charfile, outfile, players):
    self.p1_name, self.p2_name = players
    self.n1.text = self.p1_name
    self.n2.text = self.p2_name

    progress = SmashDownProgress()
    if progress.total_matches == 0:
      self.sd = SmashDown(charfile, outfile, players)
    else:
      self.sd = SmashDown(progress, outfile)
    
    p1_color = Color(self.sd.players[self.p1_name].color)
    p1_color.a = .7
    p2_color = Color(self.sd.players[self.p2_name].color)
    p2_color.a = .7
    
    self.n1.bg_color = p1_color.as_tuple()
    self.n2.bg_color = p2_color.as_tuple()
    
    self.sd.deal_chars()
    self.update_display()

  def get_player_score_status(self):
    ps = self.sd.get_player_wins_map()
    ws = sorted(ps, key=ps.get, reverse=True)
    nm = self.sd.total_matches
    cm = self.sd.completed_matches
    w1, w2 = ws[0], ws[1]
    w1s, w2s = ps[w1], ps[w2]

    sts = {player:'' for player in ps}

    if w1s + 1 > nm//2:
      sts[w1] = '(adv)'
    if w1s > w2s + (nm - cm):
      sts[w1] = 'win!'
    if w2s + (nm - cm) < w1s:
      sts[w2] = 'lose!'

    if w1s == w2s and cm == nm:
      sts[w1] = 'tie!'
      sts[w2] = 'tie!'
    elif w1s == w2s and cm + 1 == nm:
      sts[w1] = '!!!'
      sts[w2] = '!!!'

    return sts

  def update_display(self):
    chars = self.sd.get_player_char_map()
    wins = self.sd.get_player_wins_map()
    c1 = chars[self.p1_name]
    c2 = chars[self.p2_name]
    self.c1.text = c1
    self.c2.text = c2
    self.i1.image = ui.Image.named('imgs/%s_0.png' % c1)
    self.i2.image = ui.Image.named('imgs/%s_0.png' % c2)
    self.bg1.image = ui.Image.named('imgs/%s_bg.jpg' % c1)
    self.bg2.image = ui.Image.named('imgs/%s_bg.jpg' % c2)
    
    # cool proof of concept for player-tinted backgrounds, but SUPER inefficient for these purposes.
    #p1_color = self.sd.players[self.p1_name].color
    #p2_color = self.sd.players[self.p2_name].color
    #self.bg1.image = img_utils.pil2ui(img_utils.tint_bw_image(Image.open('imgs/%s_bwbg.jpg' % c1), p1_color))
    #self.bg2.image = img_utils.pil2ui(img_utils.tint_bw_image(Image.open('imgs/%s_bwbg.jpg' % c2), p2_color))

    self.score1.text = str(wins[self.p1_name])
    self.score2.text = str(wins[self.p2_name])

    self.adv1.text = ''
    self.adv2.text = ''
    p1w = wins[self.p1_name]
    p2w = wins[self.p2_name]
    sts = self.get_player_score_status()
    self.adv1.text = sts[self.p1_name]
    self.adv2.text = sts[self.p2_name]

    if self.game_over:
      self.btn_reset.hidden = False
      self.btn_p1_win.hidden = True
      self.btn_p2_win.hidden = True
      self.btn_swap.hidden = True
      infotext = 'Game Over! '
      if p1w > p2w:
        infotext += '%s Wins!' % self.p1_name
      elif p1w < p2w:
        infotext += '%s Wins!' % self.p2_name
      else:
        infotext += "It's a tie!"
      self.info.text = infotext
    else:
      self.btn_reset.hidden = True
      self.btn_p1_win.hidden = False
      self.btn_p2_win.hidden = False
      self.btn_swap.hidden = False
      infotext = 'Round %s of %s. ' % (self.sd.cur_match_num, self.sd.total_matches)
      if self.sd.num_matches_left > 0:
        infotext += '%s match%s left after this one.' % (self.sd.num_matches_left, 'es' if self.sd.num_matches_left > 1 else '')
      else:
        infotext += 'Final match!'
      self.info.text = infotext

  def swap(self, sender):
    if not self.game_over:
      self.sd.swap_chars(self.p1_name, self.p2_name)
    self.update_display()

  def reset(self, sender):
    self.sd.reset()
    self.sd.deal_chars()
    self.game_over = False
    self.update_display()

  def p1_win(self, sender):
    if not self.game_over:
      self.sd.winner(self.p1_name)
      if self.sd.num_matches_left > 0:
        self.sd.deal_chars()
      else:
        self.game_over = True
      self.update_display()

  def p2_win(self, sender):
    if not self.game_over:
      self.sd.winner(self.p2_name)
      if self.sd.num_matches_left > 0:
        self.sd.deal_chars()
      else:
        self.game_over = True
      self.update_display()

  @staticmethod
  def load_view(charfile, outfile, players):
    v = ui.load_view()
    v.init(charfile, outfile, players)
    return v


if __name__ == '__main__':
  v = SmashDownUI.load_view('data/characters.txt', 'data/history_temp.txt', ['Father1337', 'Valfor'])
  v.present(orientations=['landscape'], hide_title_bar=True)

