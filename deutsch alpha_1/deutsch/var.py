# AUTHOR: JAKOB WILMS

import cache


def add_var(arg):
    arg = arg[1:]
    arg = remove_spaces(arg)
    name, value = get_var(arg)
    i = 0
    for var_name in cache.VAR_NAMES:
        if var_name == name:
            break
        i += 1
    if i == len(cache.VAR_NAMES):
        cache.VAR_NAMES.append(name)
        cache.VAR_VALUES.append(value)
    else:
        cache.VAR_VALUES[i] = value


def remove_spaces(arg):
    output = ''
    for character in arg:
        if character != ' ':
            output += character
    return output


def get_var(arg):
    first_value_char = True
    string = False
    number = True
    dot = False
    naming = True
    name = ''
    value = None
    i = 0
    for character in arg:
        if character == '=':
            naming = False
        elif naming:
            name += character
            i += 1
        else:
            if first_value_char:
                if character == '"':
                    string = True
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
        if dot:
            value = float(arg[i+1:])
        else:
            value = int(arg[i+1:])
    return name, value
