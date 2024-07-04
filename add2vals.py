'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

argnumbers = len(sys.argv) - 1

if argnumbers < 2 :
    '''
    If the number of arguments is not 2, the program will print an error message
    to the console and provide the user with the correct usage of the program.
    '''
    print("")
    print("You entered " + str(argnumbers) + " value/s.")
    print("")
    print("Usage: 'add2vals X Y' where X and Y are individual values.")
    print("       If add2vals is not in your path, usage is './add2vals X Y'.")
    print("       If unbundled, usage is 'python add2vals.py X Y'.")
    print("")
    sys.exit(1)
else: 
    '''
    If the number of arguments is at least of 2, the program will add all the values together.
    The result is then printed to the console.
    '''
    print("")
    print("The result is " + str(calc.add2(*list(map(str, sys.argv[1:])))))
    print("")
    sys.exit(0)