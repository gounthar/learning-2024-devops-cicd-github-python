def conv(val):
    try:
        return float(val)
    except ValueError:
        return val

def add2(*args):
    somme = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            somme += arg
        elif isinstance(arg, str):
            converted = conv(arg)
            if isinstance(converted, (int, float)):
                somme += converted
            else:
                somme = str(somme) + converted
    return somme
