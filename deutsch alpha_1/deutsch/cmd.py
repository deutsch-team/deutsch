# AUTHOR: JAKOB WILMS
import sys

import cmdschreibe
import util
import var
import cache


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


def cmd(text, current_char):
    i = util.get_next_dot(text, current_char)
    if i != -1:
        arg = text[current_char:i]
        print(str(arg))
        if is_schreibe(arg):
            schreibe(arg[9:])
        elif is_variable(arg):
            var.add_var(arg)
            print(cache.VAR_NAMES)
            print(cache.VAR_VALUES)
        else:
            util.error("Invalid Syntax")
            sys.exit()
        if i == len(text) - 1:
            sys.exit()
        cmd(text, i + 1)
    else:
        util.debug("EXIT")
        sys.exit()
