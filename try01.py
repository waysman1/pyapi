#!/usr/bin/env python3

while True:     #creates a loop
    try:
       # pull info from local user
       name = input('Enter a file name: ')
       with open(name, "w") as myfile:
           myfile.write('Well done\n')
     except:
         print("Error in creating that file... try again!")
     else:
         print("File created successfully!")
         break
