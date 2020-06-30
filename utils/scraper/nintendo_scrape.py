
import urllib.request
import os

filebase = '../../imgs'
urlbase = 'https://www.smashbros.com/assets_v2/img/fighter'
MAINSONLY = True

# In only the thumbnail section, the following american names for characters
# are referred to by their japanese counterparts instead. This dictionary
# contains the necessary name substitutions to find the thumbnail files.
thumb_alts = {
	'incineroar':'gaogaen',
	'isabelle':'shizue',
	'piranha_plant':'packun_flower',
}

chars = []
with open('nintendo_chars.txt') as f:
	chars = [line.strip() for line in f.readlines()]

def make_url(urlbase, fighter_url, file):
	return '{}/{}/{}'.format(urlbase, fighter_url, file)

def make_filename(filebase, file_name, filetype):
	return '{}/{}.{}'.format(filebase, file_name, filetype)

def download_file(url, file, force=False):
	print('  Downloading: {} ...'.format(file), end='')
	if force or not os.path.exists(file):
		urllib.request.urlretrieve(url, file)
		print('Done')
	else:
		print('Skipping')

def download_additional_assets(urlname, charname):
	bgurl = make_url(urlbase, urlname, 'bg.jpg')
	bgfile = make_filename(filebase, '{}_bg'.format(charname), 'jpg')
	download_file(bgurl, bgfile)

	fnameurl = make_url(urlbase, urlname, 'fighter_name.svg')
	fnamefile = make_filename(filebase, '{}_name'.format(charname), 'svg')
	download_file(fnameurl, fnamefile)

	markurl = make_url(urlbase, urlname, 'mark.svg')
	markfile = make_filename(filebase, '{}_mark'.format(charname), 'svg')
	download_file(markurl, markfile)

	name = urlname if urlname not in thumb_alts else thumb_alts[urlname]

	thumbvurl = make_url(urlbase, 'thumb_v', '{}.png'.format(name))
	thumbvfile = make_filename(filebase, '{}_thumbv'.format(charname), 'png')
	download_file(thumbvurl, thumbvfile)

	thumbhurl = make_url(urlbase, 'thumb_h', '{}.png'.format(name))
	thumbhfile = make_filename(filebase, '{}_thumbh'.format(charname), 'png')
	download_file(thumbhurl, thumbhfile)

def download_character_assets(urlname, charname, mainonly=True):
	upper = 2 if mainonly else 9
	for i in range(1, upper):
		end = 'main{}.png'.format('' if i == 1 else i)
		url = make_url(urlbase, urlname, end)
		filename = make_filename(filebase, '{}_{}'.format(charname, i-1), 'png')
		download_file(url, filename)
	download_additional_assets(urlname, charname)

def download_mii_fighter_assets(urlname, charname):
	url = make_url(urlbase, urlname, 'main_en.png')
	filename = make_filename(filebase, '{}_0'.format(charname), 'png')
	download_file(url, filename)
	download_additional_assets(urlname, charname)



if __name__ == '__main__':
	for i, char in enumerate(chars):
		urlname, charname = char.split('\t')
		print("Downloading {}. {}/{} ({:.1%})".format(charname, i+1, len(chars), (i+1)/len(chars)))
		if charname == 'Mii Fighter':
			download_mii_fighter_assets(urlname, charname)
		else:
			download_character_assets(urlname, charname, MAINSONLY)
	print("Done.")
