from get_piece_images import get_real_time_images_of_board
import json
import cv2
import pyautogui
from stockfish import Stockfish
import time
stockfish = Stockfish("/opt/homebrew/bin/stockfish")

def convert_images_to_fen():

    get_real_time_images_of_board()

    to_move_img = pyautogui.screenshot(region=(709, 504, 228, 33))
    to_move_img.save(f"piece_images/real_time/to_move.png")

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

            if similarity >= 0.85:
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
    white_to_move = cv2.imread(f"piece_images/library/white_to_move.png")
    black_to_move = cv2.imread(f"piece_images/library/black_to_move.png")
    actual = cv2.imread("piece_images/real_time/to_move.png")

    result1 = cv2.matchTemplate(white_to_move, actual, cv2.TM_CCOEFF_NORMED)
    similarity1 = result1.max()

    result2 = cv2.matchTemplate(black_to_move, actual, cv2.TM_CCOEFF_NORMED)
    similarity2 = result2.max()

    if similarity1 > similarity2:
        fen += " w"
    else:
        fen += " b"


    return fen

def find_best_move(fen):
    stockfish.set_fen_position(fen)
    return stockfish.get_best_move()

def do_best_move(move):

    first_part1 = move[0]
    first_part2 = move[1]
    second_part1 = move[2]
    second_part2 = move[3]
    match first_part1:
        case "a":
            x1 = 329
        case "b":
            x1 = 329 + 50 * 1
        case "c":
            x1 = 329 + 50 * 2
        case "d":
            x1 = 329 + 50 * 3
        case "e":
            x1 = 329 + 50 * 4
        case "f":
            x1 = 329 + 50 * 5
        case "g":
            x1 = 329 + 50 * 6
        case "h":
            x1 = 329 + 50 * 7

    y1 = 513 + 50 * (8 - int(first_part2))

    pyautogui.moveTo(x1, y1, duration=0.1)
    pyautogui.click()

    match second_part1:
        case "a":
            x1 = 329
        case "b":
            x1 = 329 + 50 * 1
        case "c":
            x1 = 329 + 50 * 2
        case "d":
            x1 = 329 + 50 * 3
        case "e":
            x1 = 329 + 50 * 4
        case "f":
            x1 = 329 + 50 * 5
        case "g":
            x1 = 329 + 50 * 6
        case "h":
            x1 = 329 + 50 * 7

    y1 = 513 + 50 * (8 - int(second_part2))

    pyautogui.moveTo(x1, y1, duration=0.1)
    pyautogui.click()

def main():
    fen = convert_images_to_fen()
    print(f"FEN: {fen}")
    best_move = find_best_move(fen)
    print(f"Best move: {best_move}")
    do_best_move(best_move)


main()