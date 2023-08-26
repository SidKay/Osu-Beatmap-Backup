# Extracts the beatmap ids??

import os

path = "C:/Users/Sidney Anya/AppData/Local/osu!/Songs"

with open('beatmaps.txt', 'w') as bm:
	print('\n'.join(os.listdir(path)), file=bm)

content = []
for line in os.listdir(path):
	content.append(line.split(' ')[0])

with open('id.txt', 'w') as tags:
	print('\n'.join(content), file=tags)

print('Done!')