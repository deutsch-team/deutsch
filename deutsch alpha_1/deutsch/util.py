# AUTHOR: JAKOB WILMS

ENDING_SHORT = ".de"
ENDING_LONG = ".deutsch"


def debug(message):
    print("  [DEBUG] >>", message)


def error(message):
    print("  [ERROR] >>", message)


def get_next_dot(text, current_char):
    i = current_char
    text = text[current_char:]
    for character in text:
        if character == '.':
            return i
        i += 1
    return -1


def remove_line_breaks(data):
    removed = data.replace('\n', '')
    removed = removed.replace('\r', '')
    return removed


def remove_spaces_after_dots(text):
    output = ''
    string = False
    dot = False
    for character in text:  # Iterate through all characters
        if character == '"':  # In a String no Spaces should be removed
            if string:
                string = False
            else:
                string = True
            output += character  # Append character to output
        elif character == '.':
            dot = True
            output += character  # Append character to output
        elif dot:
            if character != ' ':  # If Character is ' ', nothing should happen
                dot = False
                output += character  # Append character to output
        else:
            output += character  # Append character to output
    return output
