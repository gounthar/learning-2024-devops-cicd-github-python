# ./calc.py

def conv(value):
    """
    Convert the value to an integer, float, or string.
    """
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return str(value)

def add2(*args):
    """
    Add or concatenate multiple arguments.
    """
    argsconv = [conv(arg) for arg in args]
    print("Converted Arguments:", argsconv)  # Debug line

    # Check if there are any string arguments
    string_present = any(isinstance(arg, str) for arg in argsconv)

    if string_present:
        # Concatenate all as strings
        result = ''.join(map(str, argsconv))
        print("Concatenated Result:", result)  # Debug line
        return result
    else:
        # Sum all, treating integers as floats if any float is present
        result = sum(float(arg) if isinstance(arg, (int, float)) else 0 for arg in argsconv)
        print("Float Sum Result:", result)  # Debug line
        return result

def addAll(args):
    """
    Add or concatenate all arguments in a list.
    """
    argsconv = [conv(arg) for arg in args]
    print("Converted Arguments:", argsconv)  # Debug line

    if any(isinstance(arg, str) for arg in argsconv):
        return ''.join(map(str, argsconv))
    elif any(isinstance(arg, float) for arg in argsconv):
        return sum(float(arg) if isinstance(arg, (int, float)) else 0 for arg in argsconv)
    else:
        return sum(argsconv)
