#AUTHOR: Lion Dannhorn #CONTACT: lion.dannhorn@gymnasium-oedeme.de
import os                                   #Used to open and read files
import sys                                  #Used to get the parameters specified at the launch of the program via the cmd or terminal
from datetime import datetime               #Used to provite date and time of an error in the errorlog.





def debug(message):                         #This function creates a debug message, so you don't have to write the [DEBUG] every time you want to debug.
    print('   [DEBUG] >>',message)

def debugtext(message):                     #This function is basically the debug() function, but you can print texts with multiple lines with it.

    

    file = open(message)
    print('\n','  [DEBUG FILE',message,'] [',linesInFile,'Lines ]')                 #Prints useful information as a sort of header for the actual text.
    print(file.read())                                                              #Prints the file.
    print('   [DEBUG FILE OVER]')                                                   #Shows you, that the file is over.
    file.close()

####################################################################################################################################################################################
####################################################################################################################################################################################

### STARTUP ROUTINE ###
print('\n')

args = sys.argv[1:]                         ##Save all given cmd arguments as a list args. Delete the first entry in the list, as it is only the filename, which is not relevant for further operations.
print('[Given arguments]:',args,'\n')       ##
file = open(args[0])                        ##Opens the file specified in the parameter of the execution in 'read' mode.                  ### OPENS FILE ###

fileName = os.path.basename(file.name)
fileNameAsList = list(os.path.basename(file.name))                                                                   ##This checks if the file is a .de or .deutsch file.
if fileNameAsList[-1] == 'e' or 'E' and fileNameAsList[-2] == 'd' or 'D' and fileNameAsList[-3] == '.':              ##
    fileIsDE = True                                                                                                  ##
    print('[File has the correct format.]','\n')                                                                     ##Prints out if ithe file is a .de or .deutsch
elif fileNameAsList[-1] == 'h' or 'H' and fileNameAsList[-2] == 'c' or 'C' and fileNameAsList[-3] == 's' or 'S' and fileNameAsList[-4] == 't' or 'T' and fileNameAsList[-5] == 'u' or 'U' and fileNameAsList[-6] == 'e' or 'E' and fileNameAsList[-7] == 'd' or 'D' and fileNameAsList[-7] == '.':
    fileIsDE = True                                                                                                  ##
    print('[File has the correct format.]','\n')                                                                     ##Prints out if ithe file is a .de or .deutsch
else:                                                                                                                ##
    fileIsDE = False                                                                                                 ##
    print('[File is not a .de file. This may or may not be a problem.]','\n')                                        ##Prints out if ithe file is not a .de or .deutsch


linesInFile = 0                                        ##
for line in file:                                      ##This block of code counts the lines in a file and prints it.
    	linesInFile += 1                               ##
print('[Length of file]:',linesInFile,'lines.','\n')   ##

file.close()                                                                                                                              ### CLOSES FILE ###

####################################################################################################################################################################################
####################################################################################################################################################################################

### COMMAND FUNCTIONS ###

def CMDschreibe(arguments):

    print()



### START INTERPRETING ###                      # Given variables: file, linesInFile, fileIsDE, fileNameAsList, fileName, args                # File is still opened

print('[Starting the program]','\n')



file = open(args[0])                                                                                                                      ### OPENS FILE ###

programCode = []

for i in range(linesInFile):                                        ##Line reading loop
    currentLine = file.readline()                                   ##Save current line as currentLine
    currentLineSplit = list(currentLine)                            ##Split the currentline into characters
    if '\n' in currentLineSplit:                                    ##If statement that triggers on line breaks in the code
        currentLineSplit.remove('\n')                               ##Removes the line break from the code
    programCode.extend(currentLineSplit)                            ##Appends the current line to the programCode list
    



print(programCode)      # DEBUG #

current = 0
while True:
    letter = programCode[current]
    






####################################################################################################################################################################################
####################################################################################################################################################################################


### END ROUTINE ###

print('\n')
