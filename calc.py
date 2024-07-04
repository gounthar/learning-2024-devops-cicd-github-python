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
    Add multiple arguments together. If any argument is a string, all arguments are concatenated as strings.
    
    *args: A variable number of arguments which can be integers, floats, or strings.
    
    Returns:
    int, float, or str: The sum of the arguments if all are numeric, or a concatenated string if any argument is a string.
    """

    total = 0
    for arg in args:
        if isinstance(total, (int, float)) and isinstance(arg, (int, float)):
            total += arg
        else:
            total = str(total) + str(arg)

    return total
