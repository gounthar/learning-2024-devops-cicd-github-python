def conv(value):
    '''
    Convert 'value' to the appropriate type (int, float, str) if necessary.

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
    Add multiple values together. If any value is a string, concatenate them.

    Parameters:
    *args (int, float, str): Values to be added or concatenated.

    Returns:
    int, float, str: The result of the addition or concatenation.
    """
    if not args:
        return 0

    result = args[0]
    for arg in args[1:]:
        if isinstance(result, (int, float)) and isinstance(arg, (int, float)):
            result += arg
        else:
            result = str(result) + str(arg)

    return result