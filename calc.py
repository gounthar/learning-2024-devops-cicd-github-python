in quotes (i.e. as a string).
'''


def conv(value):
    '''
    If 'value' is not an integer, convert it to a float and failing that, a string.

        except ValueError:
            return str(value)


def add2(arg1, arg2):
    '''
    The 'add2' function itself. It takes two arguments, converts them to their appropriate types

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
