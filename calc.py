def add2(*args):
    '''
    La fonction 'add2' prend un nombre illimité d'arguments et les ajoute ensemble.
    Si un des arguments est une chaîne de caractères, tous les arguments sont convertis en chaînes.

    Parameters:
    *args (int, float, str): Les valeurs à ajouter.

    Returns:
    int, float, str: Le résultat de l'addition ou de la concaténation.
    '''
    # Convertir tous les arguments à leurs types appropriés
    conv_args = [conv(arg) for arg in args]
    
    # Si un des arguments est une chaîne de caractères, les convertir tous en chaînes
    if any(isinstance(arg, str) for arg in conv_args):
        conv_args = [str(arg) for arg in conv_args]
    
    # Initialiser le résultat
    result = conv_args[0]
    
    # Ajouter tous les arguments ensemble
    for arg in conv_args[1:]:
        result += arg
        
    return result
