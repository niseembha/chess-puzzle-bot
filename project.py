from get_piece_images import get_real_time_images_of_board
import json
import cv2

def convert_images_to_fen():

    # get_real_time_images_of_board(True)

    fen_dict = {
        "a8": ".", "b8": ".", "c8": ".", "d8": ".", "e8": ".", "f8": ".", "g8": ".", "h8": ".",
        "a7": ".", "b7": ".", "c7": ".", "d7": ".", "e7": ".", "f7": ".", "g7": ".", "h7": ".",
        "a6": ".", "b6": ".", "c6": ".", "d6": ".", "e6": ".", "f6": ".", "g6": ".", "h6": ".",
        "a5": ".", "b5": ".", "c5": ".", "d5": ".", "e5": ".", "f5": ".", "g5": ".", "h5": ".",
        "a4": ".", "b4": ".", "c4": ".", "d4": ".", "e4": ".", "f4": ".", "g4": ".", "h4": ".",
        "a3": ".", "b3": ".", "c3": ".", "d3": ".", "e3": ".", "f3": ".", "g3": ".", "h3": ".",
        "a2": ".", "b2": ".", "c2": ".", "d2": ".", "e2": ".", "f2": ".", "g2": ".", "h2": ".",
        "a1": ".", "b1": ".", "c1": ".", "d1": ".", "e1": ".", "f1": ".", "g1": ".", "h1": "."
    }

    with open("images.json", "r") as f:
        real_board_images = json.load(f)

    with open("piece_images/library/images.json", "r") as f:
        library_board_images = json.load(f)

    for piece in real_board_images:

        for key, value in library_board_images.items():

            image1 = cv2.imread(f"piece_images/real_time/{piece}")
            image2 = cv2.imread(f"piece_images/library/{key}")

            result = cv2.matchTemplate(image1, image2, cv2.TM_CCOEFF_NORMED)
            similarity = result.max()

            if similarity >= 0.9:
                fen_dict[piece[:2]] = value

    fen_list = []
    count = 0
    for piece in fen_dict:
        if count == 8:
            fen_list.append("/")
            count = 0
        fen_list.append(fen_dict[piece])
        count += 1

    i = 0
    fen_list_1 = []
    fen = ""
    count = 0
    for character in fen_list:
        # every time you see a dot, check if next character is a dot, if it is, keep iterating and adding to count, if it isn't replace all dots 
        # behind where you are with the current count and then reset count to 0
        if character == ".":
            count += 1
            if i == 70:
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

    # Find out if its white to move or black to move
    

    print(fen)

convert_images_to_fen()