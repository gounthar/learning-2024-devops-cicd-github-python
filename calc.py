def conv(val):
    try:
        return float(val)
    except ValueError:
        return val

def add2(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        somme = 0
    else:
        somme = ''
    
    for arg in args:
        if isinstance(arg, (int, float)):
            if isinstance(somme, (int, float)):
                somme += arg
            else:
                somme += str(arg)
        elif isinstance(arg, str):
            converted = conv(arg)
            if isinstance(converted, (int, float)):
                if isinstance(somme, (int, float)):
                    somme += converted
                else:
                    somme += str(converted)
            else:
                somme += converted
    return somme
