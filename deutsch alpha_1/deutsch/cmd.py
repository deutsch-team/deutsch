# AUTHOR: JAKOB WILMS
import sys

import cmdschreibe
import util


def is_schreibe(arg):
    if arg[0:9] == 'schreibe ':
        return True
    else:
        return False


def schreibe(args):
    cmdschreibe.cmd_schreibe(args)


def cmd(text, current_char):
    i = util.get_next_dot(text, current_char)
    if i != -1:
        arg = text[current_char:i]
        if is_schreibe(arg):
            schreibe(arg[9:])
        else:
            util.error("Invalid Syntax")
            sys.exit()
        if i == len(text) - 1:
            sys.exit()
        cmd(text, i + 1)
    else:
        util.debug("EXIT")
        sys.exit()