# ./calc.py

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
    '''
    The 'add2' function itself. It takes multiple arguments, converts them to their appropriate types
    using the 'conv' function, and adds them together. If any argument is a string, it ensures
    all are strings before concatenating them.

    Parameters:
    *args (int, float, str): Variable number of values to be added or concatenated.

    Returns:
    int, float, str: The result of the addition or concatenation.
    '''
    # Convert each argument in '*args' to its appropriate type
    argsconv = [conv(arg) for arg in args]

    # Determine if any argument is a string
    string_present = any(isinstance(arg, str) for arg in argsconv)

    # If any argument is a string, ensure all are strings
    if string_present:
        return ''.join(map(str, argsconv))
    else:
        return sum(argsconv)
