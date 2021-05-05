# AUTHOR: JAKOB WILMS

import os
import sys
from cmd import cmd
import util

###########################################
###########################################

# START #
print("\n")

args = sys.argv[1:]  # Save arguments
util.debug("Arguments: \n")
for arg in args:
    util.debug(arg)  # Print all arguments
file = open(args[0], "r")  # Open File in 'read' mode
fileName = os.path.basename(file.name)
if fileName[-3:] == util.ENDING_SHORT:  # Check if the file has the correct format
    util.debug("Correct Format [.de]")
elif fileName[-7:] == util.ENDING_LONG:  # Check if the file has the correct format
    util.debug("Correct Format [.deutsch]")
else:  # Wrong Format
    util.error("No .de or .deutsch File.")
    continuing = input("Continue anyway? [Y/N] ")  # You can continue, even if it isn't a .de / .deutsch file
    if continuing == "N" or continuing == "n":
        sys.exit()  # Exit
data = file.read()  # Read File
file.close()  # Close File
text = util.remove_line_breaks(data)  # Remove Line Breaks
text = util.remove_spaces_after_dots(text)

###########################################
###########################################

# START INTERPRETING #
cmd.cmd(text, 0)

###########################################
###########################################

# END #
print('\n')
