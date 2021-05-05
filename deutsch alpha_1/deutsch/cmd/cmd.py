# AUTHOR: JAKOB WILMS
import sys

import cmdschreibe
from .. import util
from .. import var


def is_schreibe(arg):
    if arg[0:9] == 'schreibe ':
        return True
    else:
        return False


def is_variable(arg):
    if arg[0] == '€':
        return True
    else:
        return False


def schreibe(args):
    cmdschreibe.cmd_schreibe(args)


def add_var(args):
    var.add_var(args)


def cmd(text, current_char):
    i = util.get_next_dot(text, current_char)  # Get Pos of Next dot
    if i != -1:  # -1 = No Dot found
        arg = text[current_char:i]  # From Current Char to Dot
        if is_schreibe(arg):  # 'schreibe '
            schreibe(arg[9:])
        elif is_variable(arg):  # Variable declared
            add_var(arg)
        else:  # No Method Found
            util.error("Invalid Syntax")
            sys.exit()
        if i == len(text) - 1:  # Last Dot, Can exit
            sys.exit()
        cmd(text, i + 1)  # Repeat
    else:
        util.debug("EXIT")
        sys.exit()
