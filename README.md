# Chess Puzzle Auto-Solver Bot ♟️

A Python bot that auto-solves online chess puzzles using image recognition and Stockfish. It specifically does the Mate in Three Problems from the [Mate in Three Problems at chesspuzzles.com](https://www.chesspuzzles.com/mate-in-three). This was for my CS50 Python final project.

This bot is designed specifically for my screen size and coordinate layout. All of the board positions and screenshot regions are hard-coded for my display, so the bot only works on my device unless those coordinates are recalibrated.

## ⚠️ NOTE:

I intentionally used the site chesspuzzles.com, as there is no leaderboard or ranking system. I chose this site because what I am doing is technically “cheating” at puzzle solving, and I did not want this project to affect anyone’s ratings, standings, or competitive integrity. This bot is purely for educational and experimental purposes, and it should not be used on any platform where automated assistance violates the rules or impacts other players.

## Video Demo: <URL HERE>

(to do)

## Tools & Libraries:

**PyAutoGUI** — captures board screenshots, moves the mouse, and clicks to play moves.

**OpenCV (cv2)** — performs image matching to identify pieces and determine whose turn it is.

**Stockfish** — calculates the best mate-in-three moves and updates its internal position.

**Pynput** — listens for the ESC key to safely stop the bot at any time.

**JSON** — stores reference piece images and mapping data used during recognition.

## Description:

### Creating the library

At the start, I planned to web scrape the chess board information using Beautiful Soup, but I came into many problems, like: (state problems)

Then I began messing with PyAutoGUI, and I realized I could take screenshots with it. So, that was my plan to get the chessboard from the web to code.

For the program to actually run, I had to build a library of photos of the chess pieces to cross-reference with the real-time board, so I made that library using PyAutoGUI and some looping. I had to do a lot of testing to see which exact coordinates each square on the chessboard was. I got photos of each piece, black and white, in each background, dark and white. I had a total of 24 images so far. (6 pieces, 2 different piece colors, 2 different background colors). Then I had to add two other images to the library - images for detecting whose move it is. After taking those two photos using the same process and more experimenting with the exact coordinates, I was done with my library.

### Taking images of the board in real-time and evaluating what piece was on each square

First, the program takes screenshots of every single square on the current chessboard. In total, it has 64 photos, of all squares from a8 to h1. Then, it has the huge task of identifying each image with the correct piece, or if it's empty. To do this, I created a nested loop. It would loop through each photo of all 64 squares, and in that, it would loop through all the library photos. It would do this by using the JSONs I made for both the library and real-time images. It would compare the current library photo with the current real-time square photo using the cv2.matchTemplate() function. Then, if the similarity was greater than 85%, it would add the piece name to the dictionary I created before the loop.

The dictionary was ordered from a8 to h1 with the key as the square notation and the value as the piece. The dictionary, before the loop, had all values set to "." So, after the loop, the dictionary had the entire board completed. Each time there was a "." meant there was no piece, and if there was a piece, then the letter of the piece would be there.

I intentionally created the dictionary this way because for Stockfish to find the best move for the position, it had to read the FEN. FEN is basically (...).

### Converting dictionary to FEN notation:

Here is a brief list of FEN notation:

- Pawn: p
- Rook: r
- Knight: n
- Bishop: b
- Queen: q
- King: k
- Empty space: # of empty spaces
- New row: /

If the piece is black, keep it lowercase. If the piece is white, capitalize it.

Because of this, when making the JSON for the library images, I had the key as the file name for the photo, but the key as the FEN notation name.

Then, with the dictionary created, I iterated through it and appended it to a new list. Every time it got to the 8th iteration (end of a row), I would append a "/".

I then made an empty string and iterated through this new list to put each letter into the empty string in the correct order. I also replaced all "." with the number of consecutive "."s. I did this by checking if the next value in the list is a "." If it were, I would add 1 to the count, and if it wasn't, I would add the current count to the string and reset it to 0.

After all of this, the FEN was almost done. At the start of the program, it also takes a screenshot of where the text of whose turn it is to move and compares it with the white_to_move image and black_to_move image in the image library using the same cv2 function. Whichever photo had a higher similarity would be the correct one and would correspond to whose move it is. If it were black to move, I would add a space to the end of the FEN and then "b," and if it were white, I would add a space and then "w".

With this, the FEN was done.

### Finding the best move and moving the mouse to do the best move

Then I used the stockfish.get_best_move() function and got the best move. The first two letters would be the file and rank of the piece to move, and the second two letters would be the file and rank of the square the piece had to move to. So I would have two squares' coordinates to calculate

I first found the exact coordinate of the top left square (a8) as 329, 513. To move to the square to the right, I would add 50 to the x, and to move down, I would add 50 to the y. Then I would match each letter a,b,c,d,e,f,g,h with values 0,1,2,3,4,5,6,7. This would be how many times I would multiply the x value by 50. This would give me the correct file. To find the correct rank, I would do basically the same thing. I would multiply the top left y value of 513 by 8 minus the rank number.

Then, with the x and y dimensions of the first square and second square, I would move the mouse to the first position, click, and then move to the second position.

This was the first move done.

### Looping it

However, these were mate in three problems. So, then I would update the Stockfish board with the best move using the stockfish.make_moves_from_current_position() function. Then I would calculate the best move for black (since puzzles usually do the best move for the opposing side) and update the position again, and then find the best move for white again and move the mouse to do the move. This loop would go on until checkmate was achieved (5 total moves from both sides). Then, with the puzzle completed, the program would automatically scroll down, click the "Try a new puzzle! button, and the whole process would repeat indefinitely.

Then I added a function to constantly monitor my keyboard and check when I pressed Esc to stop the program.

With that, the entire project was done.

## Bugs / Notes

The only bug this program faces is that it will sometimes be unable to classify pieces (mainly white rooks for some reason). To mitigate this, I added more images to the library. Every once in a while, it will still mess up, but very rarely now.
