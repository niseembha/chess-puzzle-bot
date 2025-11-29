import project


def test_get_name_of_real_time_image():

    assert project.get_name_of_real_time_image(1, 1) == "a8"

    assert project.get_name_of_real_time_image(8, 8) == "h1"

    assert project.get_name_of_real_time_image(4, 4) == "d5"


def test_find_coordinates_for_move():

    x1, y1, x2, y2 = project.find_coordinates_for_move("a8a7")

    assert x1 == 329
    assert y1 == 513
    assert x2 == 329
    assert y2 == 563

    x1, y1, x2, y2 = project.find_coordinates_for_move("h1h2")

    assert x1 == 329 + 50 * 7
    assert y1 == 513 + 50 * (8 - 1)
    assert x2 == 329 + 50 * 7
    assert y2 == 513 + 50 * (8 - 2)


def test_convert_fen_dict_to_fen():

    dict1 = {
        "a8": ".",
        "b8": ".",
        "c8": "r",
        "d8": ".",
        "e8": ".",
        "f8": "q",
        "g8": ".",
        "h8": "k",
        "a7": "p",
        "b7": "p",
        "c7": ".",
        "d7": ".",
        "e7": "b",
        "f7": ".",
        "g7": ".",
        "h7": ".",
        "a6": ".",
        "b6": ".",
        "c6": "b",
        "d6": ".",
        "e6": "Q",
        "f6": ".",
        "g6": ".",
        "h6": "p",
        "a5": ".",
        "b5": ".",
        "c5": ".",
        "d5": "N",
        "e5": "P",
        "f5": ".",
        "g5": ".",
        "h5": ".",
        "a4": ".",
        "b4": ".",
        "c4": ".",
        "d4": "p",
        "e4": "B",
        "f4": "r",
        "g4": ".",
        "h4": "P",
        "a3": ".",
        "b3": ".",
        "c3": ".",
        "d3": ".",
        "e3": ".",
        "f3": ".",
        "g3": ".",
        "h3": ".",
        "a2": "P",
        "b2": "P",
        "c2": ".",
        "d2": ".",
        "e2": ".",
        "f2": ".",
        "g2": ".",
        "h2": ".",
        "a1": ".",
        "b1": ".",
        "c1": "R",
        "d1": ".",
        "e1": ".",
        "f1": ".",
        "g1": "R",
        "h1": "K",
    }

    dict2 = {
        "a8": "r",
        "b8": ".",
        "c8": "b",
        "d8": ".",
        "e8": "k",
        "f8": ".",
        "g8": ".",
        "h8": "r",
        "a7": "p",
        "b7": "p",
        "c7": ".",
        "d7": ".",
        "e7": "b",
        "f7": "p",
        "g7": "p",
        "h7": "p",
        "a6": ".",
        "b6": ".",
        "c6": ".",
        "d6": ".",
        "e6": ".",
        "f6": ".",
        "g6": ".",
        "h6": ".",
        "a5": ".",
        "b5": ".",
        "c5": ".",
        "d5": "N",
        "e5": ".",
        "f5": ".",
        "g5": "q",
        "h5": ".",
        "a4": ".",
        "b4": ".",
        "c4": "p",
        "d4": ".",
        "e4": ".",
        "f4": ".",
        "g4": ".",
        "h4": ".",
        "a3": ".",
        "b3": ".",
        "c3": ".",
        "d3": ".",
        "e3": ".",
        "f3": ".",
        "g3": ".",
        "h3": ".",
        "a2": "P",
        "b2": "P",
        "c2": "P",
        "d2": ".",
        "e2": ".",
        "f2": "P",
        "g2": "P",
        "h2": "P",
        "a1": "R",
        "b1": ".",
        "c1": ".",
        "d1": "Q",
        "e1": "R",
        "f1": ".",
        "g1": "K",
        "h1": ".",
    }

    assert project.convert_fen_dict_to_fen(dict1) == "2r2q1k/pp2b3/2b1Q2p/3NP3/3pBr1P/8/PP6/2R3RK w"
    assert project.convert_fen_dict_to_fen(dict2) == "r1b1k2r/pp2bppp/8/3N2q1/2p5/8/PPP2PPP/R2QR1K1 w"
