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

def add2(arg1, arg2):
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
    # Convert 'arg1' and 'arg2' to their appropriate types
    arg1conv = conv(arg1)
    arg2conv = conv(arg2)
    # If either 'arg1' or 'arg2' is a string, ensure they're both strings.
    if isinstance(arg1conv, str) or isinstance(arg2conv, str):
        arg1conv = str(arg1conv)
        arg2conv = str(arg2conv)
    return arg1conv + arg2conv

def addAll(args):
    '''
    The 'addAll' function itself. It takes multiples arguments, converts them to their appropriate types
    using the 'conv' function, and adds them together. If either argument is a string, it ensures
    all are strings before concatenating them.
    Parameter:
    args (list): A list of values to be added.
    Returns:
    int, float, str: The result of the addition or concatenation.
    '''
    # Create an empty list to store the converted arguments
    argsconv = []

    # Convert each argument in 'args' to its appropriate type
    for arg in args:
        argsconv.append(conv(arg))

    # Create an empty string to store the result
    result = ""
    # If any of the arguments are strings, ensure all are strings
    for arg in argsconv:
        if (isinstance(arg, str) == False):
            arg = str(arg)
        result += arg

    # Return the result
    return result
