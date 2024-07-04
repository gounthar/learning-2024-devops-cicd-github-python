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

def addAll(*args):
    # tenter de convertir tous les éléments de la liste en nombres et les concaténer
    argsconv = list(map(lambda val: conv(val), args))

    # si l'un des éléments est toujours une string, convertir tous les éléments en string
    if len(list(filter(lambda val: isinstance(val, str), argsconv))):
        argsconv = "".join(map(lambda val: str(val), argsconv))
    else:
        # sinon additionner les éléments
        argsconv = sum(argsconv)
    return argsconv
