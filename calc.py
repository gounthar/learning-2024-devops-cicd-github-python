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
    """
    Ajoute un nombre d'arguments ensemble ou les concatène si ce sont des chaînes de caractères.

    Paramètres:
    *args : une séquence d'arguments de type varié (int, float, str, etc.).

    Retourne:
    - Si aucun argument n'est fourni, retourne 0
    - Si au moins un argument est une chaîne de caractères, concatène tous les argument en une seule chaîne
    - Sinon, additionne tous les argument
    """
    if not args:  
        return 0
    result = args[0]
    for arg in args[1:]:
        if isinstance(result, str) or isinstance(arg, str):
            result = str(result) + str(arg)
        else:
            result += arg
    return result

