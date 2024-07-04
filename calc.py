def conv(value):
    '''
    Si 'value' n'est pas un entier, le convertir en float et, en cas d'échec, en chaîne de caractères.

    Paramètres:
    value (int, float, str): La valeur à convertir.

    Renvoie:
    int, float, str: La valeur convertie.
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
    La fonction 'add2' prend un nombre variable d'arguments, les convertit à leur type
    approprié en utilisant la fonction 'conv', et les additionne. Si un argument est une chaîne de caractères,
    elle s'assure que tous sont des chaînes avant de les concaténer.

    Paramètres:
    *args (int, float, str): Les valeurs à additionner.

    Renvoie:
    int, float, str: Le résultat de l'addition ou de la concaténation. Si aucun argument n'est fourni,
    une chaîne vide est renvoyée.
    '''
    # Initialiser un indicateur pour vérifier si un argument est une chaîne de caractères
    has_string = False
    # Liste pour stocker les arguments convertis
    converted_args = []

    # Convertir tous les arguments et vérifier si l'un d'eux est une chaîne de caractères
    for arg in args:
        converted = conv(arg)
        if isinstance(converted, str):
            has_string = True
        converted_args.append(converted)
    
    # Si un argument est une chaîne de caractères, les convertir tous en chaînes
        if has_string:
        converted_args = [str(arg) for arg in converted_args]

    # Si aucun argument n'est fourni, renvoyer une chaîne vide
        if not converted_args:
        return ''

    # Calculer le résultat en additionnant ou en concaténant les arguments
    result = converted_args[0]
    for arg in converted_args[1:]:
        result += arg
    
    return result
