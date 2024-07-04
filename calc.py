'''
The 'calc' library contains the 'add2' function that takes 2 values and adds
them together. If either value is a string (or both of them are) 'add2' ensures
they are both strings, thereby resulting in a concatenated result.
NOTE: If a value submitted to the 'add2' function is a float, it must be done so
in quotes (i.e. as a string).
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
    Adds multiple values together. If any value is a string, converts all to strings and concatenates them.
    
    Args:
        *args: A variable length argument list of values to add or concatenate.
    
    Returns:
        The sum of all numeric values, or a concatenated string if any value is a string.
    """
    if any(isinstance(arg, str) for arg in args):
        return ''.join(map(str, args))
    return sum(args)

