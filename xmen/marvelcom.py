#!/usr/bin/env python3

import marvelous

# Your own config file to keep your private key local and secret
#from config import public_key, private_key

with open("/home/student/marvel.pub") as pbk:
    public_key = pbk.read().rstrip('\n')

with open("/home/student/marvel.priv") as privbk:
    private_key = privbk.read().rstrip('\n')

# Authenticate with Marvel, with keys I got from http://developer.marvel.com/
m = marvelous.api(public_key, private_key)

# Get all comics from this week, sorted alphabetically by title
pulls = sorted(m.comics({
    'format': "comic",
    'formatType': "comic",
    'noVariants': True,
    'dateDescriptor': "thisWeek",
    'limit': 100}),
    key=lambda comic: comic.title)

for comic in pulls:
    # Write a line to the file with the name of the issue, and the
    # id of the series
    print('{} (series #{})'.format(comic.title, comic.series.id))
