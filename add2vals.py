'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

argnumbers = len(sys.argv) - 1

if argnumbers == 2:
    '''
    If the number of arguments is 2,
    ther.
    The result is then printed to the console.
    '''
    print("")
    print(f"The result is {calc.add2(sys.argv[1], sys.argv[2])}")
    print("")
    sys.exit(0)

if argnumbers != 2:
    '''
    If the number of arguments is not 2, 
    '''
    print("")
    print(f"You entered {argnumbers} value/s.")
    print("")
    print("Usage: 'add2vals X Y' where X and Y are individual values.")
    print("       If add2vals is not in your path, usage is './add2vals X Y'.")
    print("       If unbundled, usage is 'python add2vals.py X Y'.")
    print("")
    sys.exit(1)
