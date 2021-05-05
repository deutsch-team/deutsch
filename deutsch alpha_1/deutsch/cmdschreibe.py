def cmd_schreibe(args):
    if args[0] == '"' and args[-1] == '"':  # String
        print(''.join(args[1:-1]))  # Print without '"'
    else:
        number = True
        point = False
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for arg in args:  # Iterate through all characters in args
            if arg not in numbers:  # If arg isn't a number
                if arg == ",":  # Float/Double
                    if not point:  # There can only be one '.'
                        point = True
                    else:
                        number = False
                        break  # Exit Loop
                else:
                    number = False  # Else it isn't a number
                    break  # Exit Loop
        if number:  # Print only if it is a number
            print(''.join(args))
