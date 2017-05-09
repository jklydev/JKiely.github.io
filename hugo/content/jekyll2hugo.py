"""Script to convert jekyll style posts to hugo style."""

import os

bdir = "./jekyll-posts/"
adir = "./post/"

titles = os.listdir(bdir)

dicts = [{
            'file_name': name,
            'text': open((bdir + name)).read()
        } for name in titles]

for d in dicts:
    try:
        d['body'] = d['text'].split('---')[2]
    except:
        d['body'] = d['text']

for d in dicts:
    d['name'] = ' '.join(d['file_name'].split('.')[0].split('-')[3:]).title()
    d['title'] = '-'.join(d['file_name'].split('.')[0].split('-')[3:])
    d['date'] = '-'.join(d['file_name'].split('-')[:3])

for d in dicts:
    d['header'] = "+++\ndate = \"{}\"\ntitle = \"{}\"\n\n+++\n\n".format(
            d['date'],
            d['name']
    )

for d in dicts:
    f = open((adir + d['name'] + '.md'), 'w')
    f.write(d['header'] + d['body'])
