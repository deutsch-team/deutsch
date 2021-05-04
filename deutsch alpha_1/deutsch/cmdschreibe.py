def cmd_schreibe(args):
    if args[0] == '"' and args[-1] == 0:
        print(''.join(args[1:-1]))
    else:
        number = True
        point = False
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for arg in args:
            if arg not in numbers:
                if arg == ".":
                    if not point:
                        point = True
                    else:
                        number = False
                        break
                else:
                    number = False
                    break
        if number:
            print(str(args))
