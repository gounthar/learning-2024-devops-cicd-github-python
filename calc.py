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
    '''
    The 'add2' function itself. It takes two arguments, converts them to their appropriate types
    using the 'conv' function, and adds them together. If either argument is a string, it ensures
    both are strings before concatenating them.

    Parameters:
    arg1 (int, float, str): The first value to be added.
    arg2 (int, float, str): The second value to be added.

    Returns:
    int, float, str: The result of the addition or concatenation.
    '''
    if not args:
        return 0  # Return 0 if no arguments are provided

    # Convertit les arguments dans la bon type 
    converted_args = [conv(arg) for arg in args]

    # regarde si tous les arguments sont bien des String 
    if any(isinstance(arg, str) for arg in converted_args):
        converted_args = [str(arg) for arg in converted_args]

    result = converted_args[0]
    for arg in converted_args[1:]:
        result += arg

    return result