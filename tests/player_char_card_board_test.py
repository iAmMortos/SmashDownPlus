
import test_context
from views.player_char_card_board import PlayerCharCardBoard
from player import Player

players = [Player('Father1337', 0, 'Min Min'), Player('Valfor', 1, 'Mario'), Player('DanielBoii', 2, 'Donkey Kong')]

pccb = PlayerCharCardBoard(players)
pccb.present(orientations=['landscape'], hide_title_bar=True)

