from stockfish import Stockfish
stockfish = Stockfish("/opt/homebrew/bin/stockfish")

fen = "rn3rk1/p5pp/2p5/3Ppb2/2q5/1Q6/PPPB2PP/R3K1NR b"
stockfish.set_depth(25)
stockfish.set_fen_position(fen)
print(stockfish.get_board_visual())
best_move = stockfish.get_best_move()
print(best_move)
