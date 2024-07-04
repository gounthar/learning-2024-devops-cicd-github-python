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
    The 'add2' function takes any number of arguments, converts them to their appropriate types
    using the 'conv' function, and adds them together. If any argument is a string, it ensures
    all arguments are converted to strings before concatenating them.

    Parameters:
    *args (int, float, str): Any number of values to be added together.

    Returns:
    int, float, str: The result of the addition or concatenation.
    '''
    # Initialize total to accumulate the sum
    total = conv(0)  # Start with 0 of appropriate type

    # Iterate over all arguments
    for arg in args:
        arg_conv = conv(arg)  # Convert each argument to its appropriate type

        # If any argument is a string, convert all to strings for concatenation
        if isinstance(total, str) or isinstance(arg_conv, str):
            total = str(total) + str(arg_conv)
        else:
            total += arg_conv  # Add numeric values

    return total
