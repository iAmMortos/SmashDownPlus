import test_context

import ui
from views.char_picker_tile import CharPickerTile

cpt = CharPickerTile.load_view('R.O.B.')
cpt.frame = (10, 10, 194, 46)
cpt.action = lambda s: print(cpt.char)
v = ui.View()
v.add_subview(cpt)
v.present()
