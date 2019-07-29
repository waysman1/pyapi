#!/usr/bin/python3

def main():
    hostipdict = {'host01': '10.0.0.2', 'host02': '192.168.70.1', 'host03': '8.8.8.8'}

    print(hostipdict['host02'])

    # print(hostipdict[2])   Will not work.  No key selected

    hostipdict['host04'] = '172.0.01'

    print(hostipdict)

    hostipdict.update({'host05': '9.9.9.9'})

    print(hostipdict)

    #hostipdict.get('host66')

    print(hostipdict.get('host66'))   #will return a null value, the key hasn't been defind

    print(hostipdict.keys())  # Prints the dictionary keys

    print(hostipdict.values()) # Print the dictionary values


main()    
