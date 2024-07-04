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
    Add an unlimited number of numeric arguments. If any argument is a string,
    convert all arguments to strings and concatenate them.

    Args:
        *args: Numeric arguments to add together or concatenate.

    Returns:
        str or float: Concatenated string if any argument is a string,
                      otherwise the sum of the numeric arguments.
    """
    if any(isinstance(arg, str) for arg in args):
        return ''.join(map(str, args))
    else:
        return sum(arg for arg in args if isinstance(arg, (int, float)))

