# AUTHOR: JAKOB WILMS

ENDING_SHORT = ".de"
ENDING_LONG = ".deutsch"


def debug(message):
    print("  [DEBUG] >>", message)


def error(message):
    print("  [ERROR] >>", message)


def get_next_dot(text, current_char):
    i = 0
    text = text[current_char:]
    for character in text:
        if character == '.':
            return i
        i += 1
    return -1


def remove_line_breaks(data):
    removed = data.strip('\n')  # Remove Unix Line Breaks
    removed = removed.strip('\r')  # Remove Windows Line Breaks
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
    return output
