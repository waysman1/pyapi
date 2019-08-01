#!/usr/bin/env python3
import urllib.request
import json
# api.open-notify.org/astros.json

# making request to ISS API

## Trace the ISS - earth-orbital space station
issurl = 'http://api.open-notify.org/astros.json'

## Call the webserv
trackiss = urllib.request.urlopen(issurl)

## put into file object
ztrack = trackiss.read()

## JSON 2 Python data structure
result = json.loads(ztrack.decode('utf-8'))

## display our Pythonic data
print("\n\nConverted Python data")
print(result)
input('\nISS data retrieved & converted. Press any key to continue')



