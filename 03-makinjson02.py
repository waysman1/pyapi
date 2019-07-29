#!/usr/bin/python3
import json

def main():

    # this is a list of dictionaries
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusain"}, {"name": "Arthur Dent", "species": "Human"}]

        # changes our lists of dictionaries into a JSON string
        json.dumps(hitchhikers)

        # returns the class that made the object
        print(type(hitchhikers))

        # resturns the class that made this object (str)
        print(type(jsonstring))
        
        # no surprises
        print(jsonstring)

        print(hitchhikers[0])

        print(jsonstring[0])

main()


