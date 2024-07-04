"""
The 'calc' library contains the 'add2' function that takes multiple values and adds
them together. If any value is a string, 'add2' ensures they are all strings,
thereby resulting in a concatenated result.
NOTE: If a value submitted to the 'add2' function is a float, it must be done so
in quotes (i.e. as a string).
"""

def conv(value):
    """
    If 'value' is not an integer, convert it to a float and failing that, a string.

    Parameters:
    value (int, float, str): The value to be converted.

    Returns:
    int, float, str: The converted value.
    """
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return str(value)

def add2(*args):
    """
    The 'add2' function itself. It takes multiple arguments, converts them to their appropriate types
    using the 'conv' function, and adds them together. If any argument is a string, it ensures
    all are strings before concatenating them.

    Parameters:
    *args (int, float, str): The values to be added.

    Returns:
    int, float, str: The result of the addition or concatenation.
    """
    args = [conv(arg) for arg in args]

    if any(isinstance(arg, str) for arg in args):
        args = [str(arg) for arg in args]
        return ''.join(args)
    else:
        return sum(args) if len(args) > 0 else 0
