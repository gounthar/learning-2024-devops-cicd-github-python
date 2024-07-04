'''
The 'calc' library contains the 'add2' function that takes infinite amount of values and adds
them together. If one of the values are a string (or both of them are) 'add2' ensures
they'are being ignored, thereby resulting in a addition of the result of the int and float values.
'''

def conv(value):
    '''
    If 'value' is not an integer, convert it to a float and failing that, a string.

    Parameters:
    value (int, float, str): The value to be converted.

    Returns:
    int, float, str: The converted value.
    '''
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return str(value)

def add2(*args):
    """
    Addition an infinite amount of int & float values.
    Otherwise, the value will be ignored.

    *args: args to addition.
    Returns: the addition of the args.
    """
    somme = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            somme += arg
    return somme
