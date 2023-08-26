import os
import requests
from ossapi import Ossapi

client_id = 'I don\'t know an efficient way for this.'
client_secret = 'So I\'m just going to remove these.'

api = Ossapi(client_id, client_secret)


# print(bm.title)
# print(bm.artist)
# print(bm.id)

forbidden = '\\/:*?"<>|'
translation_table = str.maketrans('', '', forbidden)

if not os.path.exists('./download'):
	os.makedirs('./download')
path = './download'

with open('id.txt') as ids:
	tags = ids.readlines()

for tag in tags:
	t = tag[:-1] if '\n' in tag else tag
	bm = api.beatmapset(beatmapset_id=t)
	title = bm.title.translate(translation_table)

	bm_name = f'{bm.id} {bm.artist} - {title}'
	fold_path = os.path.join(path, bm_name)

	try:
		os.makedirs(fold_path)
	except FileExistsError:
		print(f'Beatmap {bm_name} seems to already exist. Skipping...')
		continue

	link = f'https://osu.ppy.sh/beatmapsets/{t}/download'
	r = requests.get(link)

	if r.status_code == 200:
		with open(f'{fold_path}/{bm_name}.osz', 'wb') as m:
			print(f'Downloading {bm_name}...')
			m.write(r.content)
	else:
		print(f'Status code: {r.status_code}')

print('This should display if it\'s done.')

# Hold up
# So let me get this straight...

# When you go on the osu website
# It gives you a CSRF token (Whatever that is)
# Then it requires you to log in using that token
# THEN you can now download a beatmap?????

# ...
# I am so confused.