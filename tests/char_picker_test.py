import test_context

from views.char_picker import CharPicker

v = CharPicker.load_view()
v.present()
v.wait_modal()
print(v.result)
