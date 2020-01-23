from smashdown import SmashDown


def print_match_status(sd):
	ps = sd.get_player_names()
	pws = sd.get_player_wins_map()
	print('==========\nRound %s:' % sd.cur_match_num)
	print('  %s matches left after this one.' % sd.num_matches_left)
	print('Wins:')
	for p in ps:
		print('  %s: %s' % (p, pws[p]))
	

def smash(sd):
	sd.deal_chars()
	running = True
	ps = sd.get_player_names()
	while running:
		print_match_status(sd)
		print('---')
		pcs = sd.get_player_char_map()
		for i,p in enumerate(ps):
			print('  %s) %s: %s' % (i+1, p, pcs[p]))
		print('  ---\n  0) Swap Characters')
		inp = input('\nWho won? ')
		if inp == '0':
			sd.swap_chars()
		elif str.isdigit(inp) and int(inp) > 0 and int(inp) <= len(sd.get_player_names()):
			winner = ps[int(inp) - 1]
			print('  Congratulations, %s' % winner)
			sd.winner(winner)
			if sd.num_matches_left == 0:
				running == False
			else:
				sd.deal_chars()
		elif inp.lower() == 'quit':
			print('Bye bye.')
			running = False
			

def collect_player_names():
	running = True
	players = []
	while running:
		pn = input('Enter a player name (or blank to end): ')
		if pn != '':
			players.append(pn)
		else:
			running = False
	return players

def main():
	players = collect_player_names()
	running = False
	sd = None
	if len(players) == 0:
		print('I mean... you gotta have *players*.')
	else:
		sd = SmashDown('characters.txt', 'history.txt', players)
		smash(sd)
	

if __name__ == '__main__':
	main()

