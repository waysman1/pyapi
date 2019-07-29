#!/usr/bin/python3

import json

def main():
    # use the with statement to open file 'datacenter.json' in read olny mode
    with open("datacenter.json") as datacenter:

        #read the contents of the file-- this creates a string
        datacenterstring = datacenter.read()

    # print the string we just created
    print(datacenterstring)

    # confirms that our data is a string
    print(type(datacenterstring))

    # creates a pythonic datastructure from out string by passing through json.loads()
    datacenterdecoded = json.loads(datacenterstring)

    #confirms that our data is now a dictionary
    print(type(datacenterdecoded))

    # use our new dictionary to display the value assuc with the key 'row3'
    print(datacenterdecoded["row3"])

    print(datacenterdecoded["row2"][0])
main()


