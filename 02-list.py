#1/usr/bin/python3

def main():
    zlist = ['cisco', 'juniper', 'bigip', 'tellabs', 'meraki']

    print(zlist[2])  # List begin at zero so 2 would be the third position

    zlist.append('nortel')

    print(zlist[-1]) # You can also count from the end by counting -1 is the last position

   # zlist.extend('what does this do')  # breaks apart the value and adds it to the list

    zcloud = ['aws', 'openstack' ,'google', 'azure']

    zlist.extend(zcloud)  # adds 2 list together

    print(zlist)

main()

