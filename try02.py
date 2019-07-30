#!/usr/bin/env python3

import sys
#start with our infinite loop
while True:
    try:
        print("let 's divide x by y!")
        x = int(input("What is the integer value of x?"))
        y = int(input("What is the integer value of y?"))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as zerr:
        print("Handling of a run time error:", zerr)
    except:
        print("oh wow. We did not produce code to handle this type of error yet.")
        print(sys.exc_info()[0])
        raise 
