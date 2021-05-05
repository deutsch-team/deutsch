# AUTHOR: JAKOB WILMS

import cache
import util


def add_var(arg):  # Add new Var and Value, or change Value if var exists
    arg = arg[1:]  # Remove '€'
    arg = remove_spaces(arg)  # Remove spaces before and after '='
    name, value = get_var(arg)  # Get Name and Value
    i = get_var_pos(name)  # Get Pos
    if i == len(cache.VAR_NAMES):  # Var not existing
        cache.VAR_NAMES.append(name)  # Append Name
        cache.VAR_VALUES.append(value)  # Append Value
    else:  # Var existing
        cache.VAR_VALUES[i] = value  # Change value


def get_value(name):  # Returns: Value of the var with the name, or None
    i = get_var_pos(name)  # Get Pos
    if i == len(cache.VAR_NAMES):  # Var not existing
        return None  # Returns None
    else:  # Var existing
        return cache.VAR_VALUES[i]  # Return Value


def get_var_pos(name):  # Returns: Pos of The Var with the Name
    i = 0
    for s in cache.VAR_NAMES:  # Iterate through all names
        if s == name:  # Var found
            break
        i += 1  # Add 1
    return i  # Return pos


def remove_spaces(arg):  # Remove Spaces before and after '='
    output = ''
    for character in arg:  # Iterate through all characters
        if character != ' ':  # Add only if it isn't ' '
            output += character
    return output  # Return


def get_var(arg):
    first_value_char = True
    string = False
    number = True
    dot = False
    naming = True
    name = ''
    value = None
    i = 0
    for character in arg:  # Iterate through all Characters in arg
        if character == '=':  # Var Name is before '='
            naming = False
        elif naming:
            name += character
            i += 1  # End of Var-Name
        else:
            if first_value_char:
                if character == '"':
                    string = True
                    number = False
                    value = ""
                elif character not in cache.NUMBERS:
                    if character == ',':
                        if dot:
                            number = False
                            break
                        else:
                            dot = True
                    else:
                        number = False
                first_value_char = False
            else:
                if string:
                    if character != '"':
                        value += character
                else:
                    break
    if number:
        try:
            value = float(arg[i + 1:])
        except ValueError:
            try:
                value = int(arg[i + 1:])
            except ValueError:
                util.error("Syntax Error: Can not convert to Float / Int")
    return name, value
