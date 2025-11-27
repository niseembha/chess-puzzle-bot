
def convertHTMLtoFEN(path):

    fen_list = []
    # Goal for this:
        # Make a list (using openCV or some type of image library) of all pieces from a8 to h1 
        # (bottom right to top left for black and top right to bottom left for white)
        # reference each piece with image library and replace image with actual piece name
        # if empty square make it a dot
        # once you get to a new line make a /


    i = 0
    fen_list_1 = []
    for character in fen_list:
        # every time you see a dot, check if next character is a dot, if it is, keep iterating and adding to count, if it isn't replace all dots 
        # behind where you are with the current count and then reset count to 0
        if character == ".":
            count += 1
            if i == 71:
                if fen_list[i] == ".":
                    fen_list_1.append(count)
                break

            if fen_list[i+1] != ".":
                fen_list_1.append(count)
                count = 0

        else:
            fen_list_1.append(character)

        i += 1

    for character in fen_list_1:
        fen += str(character)

    print(fen)

convertHTMLtoFEN("test_1.html")