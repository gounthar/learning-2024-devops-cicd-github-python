'''
The 'calc' library contains the 'add' function that takes unlimited values and adds
them together. If either value is a string (or all of them are) 'add' ensures
they are all strings, thereby resulting in a concatenated result.
NOTE: If a value submitted to the 'add' function is a float, it must be done so
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

def add(*args):
    '''
    The 'add' function itself. It takes unlimited arguments, converts them to their appropriate types
    using the 'conv' function, and sums them up. If either argument is a string, it ensures
    all of them are strings before concatenating them.

    Parameters:
    *args (int, float, str): An array of values that need to be summed.

    Returns:
    int, float, str: The result of the addition or concatenation.
    '''
    # Convert 'arg1' and 'arg2' to their appropriate types
    argsconv = list(map(lambda val: conv(val), args))

    # If either 'arg1' or 'arg2' is a string, ensure they're both strings.
    if len(list(filter(lambda val: isinstance(val, str), argsconv))):
        argsconv = "".join(map(lambda val: str(val), argsconv))
    else:
        argsconv = sum(argsconv)
    return argsconv
