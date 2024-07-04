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
    The 'add2' function itself. It takes a variable number of arguments, converts them to their
    appropriate types using the 'conv' function, and adds them together. If any argument is a 
    string, it ensures all are strings before concatenating them.

    Parameters:
    *args (int, float, str): The values to be added.

    Returns:
    int, float, str: The result of the addition or concatenation.
    '''
    # Initialize a flag to check if any argument is a string
    has_string = False
    # List to store converted arguments
    converted_args = []

    # Convert all arguments and check if any is a string
    for arg in args:
        converted = conv(arg)
        if isinstance(converted, str):
            has_string = True
        converted_args.append(converted)
    
    # If any argument is a string, convert all to strings
    if has_string:
        converted_args = [str(arg) for arg in converted_args]

    # Calculate the result by summing or concatenating the arguments
    result = converted_args[0]
    for arg in converted_args[1:]:
        result += arg
    
    return result
