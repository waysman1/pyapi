#!/usr/bin/env python3

def showIntructions():
    print('''
    The objective of the game is to grab
    RPG Game
    ========
    Commands:
       go [direction]
       get [item]
    ''')

def showStatus():
    print('---------------------')
    print('you are in the ' + currentRoom)

    print('Inventory: ' + str(inventory))
    if "item" in rooms[currentRoom]:
        print("you see a " + rooms[currentRoom]['item'])
    print('----------------------')

invertory = []

rooms = {
           
            'Hall': {
                'north' : 'Store'
                'south' : 'Kitchen',
                'east' : 'Dining room',
                'item' : 'skeletonkey'
                },
            'Store' : {
                'south': 'Hall'
                'item': 'cookie'
                }
            'Kitchen' : {
                  'north' : 'Hall'
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall'
                  'south' : 'Garden',
                  'item' : 'potion'
             }
           'Garden' : {
               'north' : 'Dining Room'
               }
         }    

currentRoom = 'Hall'

showInstructions()

# loop forever
while True:
    showStatus()
    move =''
    while move =='':
        move = input('> ')
        
    move = move.lover().split() 
    # ['go', 'north']

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("you cannot go that way!")
    
    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            # inventory = inventory + [move[1]]
            # inventory.append(move[1])
            print(move[1] + "picked up!")
            del rooms[currentRoom]['item']
        else:
            print(
            if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom] ['item']:
            print(' A monster has got you...  GAME OVER!')
            break


