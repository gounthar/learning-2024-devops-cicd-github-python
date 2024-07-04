'''
The 'calc' library contains the 'add2' function that takes 2 values and adds
them together. If either value is a string (or both of them are) 'add2' ensures
they are both strings, thereby resulting in a concatenated result.
NOTE: If a value submitted to the 'add2' function is a float, it must be done so
in quotes (i.e. as a string).
'''

def conv(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return str(value)

def add2(*args):
    args = [conv(arg) for arg in args]

    if any(isinstance(arg, str) for arg in args):
        args = [str(arg) for arg in args]

        return ''.join(args)
    else:
        return sum(args)
