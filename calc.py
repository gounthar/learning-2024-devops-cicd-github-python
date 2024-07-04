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

# calc.py
def add2(*args):
    """
    Additionne plusieurs valeurs ensemble. Si une valeur est une chaîne de caractères,
    toutes les valeurs sont traitées comme des chaînes de caractères.

    Args:
        *args: Un nombre variable d'arguments qui peuvent être soit des entiers, soit des chaînes de caractères.

    Returns:
        La somme des valeurs si ce sont toutes des entiers ou des flottants, ou une chaîne de caractères concaténée si un argument est une chaîne de caractères.
    """
    try:
        return sum(float(arg) for arg in args)
    except ValueError:
        return ''.join(map(str, args))

