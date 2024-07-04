'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

argnumbers = len(sys.argv) - 1

'''
The program will add all the given values together.
The result is then printed to the console.
'''
print("")
print("The result is " + str(calc.add(*list(map(str, sys.argv[1:])))))
print("")
sys.exit(0)