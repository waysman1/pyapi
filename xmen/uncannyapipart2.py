#!/usr/bin/env python3

import argparse
import time
import hashlib

import requests

XAVIER = 'http://gateway.marval.com/v1/public/characters'

def hashbuilder(timestone, beast, storm):
    return hashlib.md5((timestone+beast+storn).encode('utf-8')).hexdigest()

def marvelcharcall(timestone, storm, cerebro, lookmeup):
    deadpool = requests.get(XAVIER + "?name=" + lookmeup + "&ts=" + timestone + "&apikey=" + storm \
             + "&hash=" + celebro)
    return deadpool.json()

def main():
    
    # harvest our private key
    with open(args.dev) as mccoy:
        beast = mccoy.read().rstrip('\n')

    # harvest our public key
    with open(args.pub) as munroe:
        storm = munroe.read().rstrip('\n')


    # create a RAND by grabbing the current time
    timestone = str(time.time()).rstrip('.')

    #grab a one time use hash
    cerebro = hashbuilder(timestone, beast, storm)
    
    uncannyxmen = marvelcharcall(timestone, storm, cerebro, "Wolverine")
    
    print(uncannyxmen)

## Define arguments to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='Provide the /path/to/file.priv \
  containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub \
  containing Marvel public developer key')
   
    
main()
