# command-line-games
My implementations of different games for entertainment that can be played in command line

# games implemented

- Othello (Reversi)

    - Players take turns placing pieces on an 8x8 board, flipping opponent's pieces.
    Black ('B') goes first. The player with the most pieces at the end wins.
    - [Detailed rules from wikipedia](https://en.wikipedia.org/wiki/Reversi)
    - Start playing: `python othello.py`

- Tic-Tac-Toe

    - Two players take turns placing X or O on a 3x3 board.
    - The first player to get three in a row (horizontally, vertically, or diagonally) wins.
    - If the board fills up with no winner, it's a tie.
    - Start playing: `python tic_tac_toe.py`

- Connect Four

    - Two players take turns dropping pieces into a 7-column, 6-row board.
    - The first player to get four in a row (horizontally, vertically, or diagonally) wins.
    - If the board fills up with no winner, it's a tie.
    - [Detailed rules from wikipedia](https://en.wikipedia.org/wiki/Connect_Four)
    - Start playing: `python connect_four.py`

- Checkers (Draughts)

    - Two players take turns moving their pieces diagonally forward on an 8x8 board.
    - Capture by jumping over opponent's pieces. No kinging or forced jumps for simplicity.
    - Black ('B') goes first. The player who captures all opponent's pieces wins.
    - [Detailed rules from wikipedia](https://en.wikipedia.org/wiki/Draughts)
    - Start playing: `python checkers.py`

- Minesweeper

    - Single player game on a 9x9 board with 10 hidden mines.
    - Uncover all non-mine cells to win. Uncovering a mine ends the game.
    - Numbers indicate how many mines are adjacent to a cell.
    - [Detailed rules from wikipedia](https://en.wikipedia.org/wiki/Minesweeper_(video_game))
    - Start playing: `python minesweeper.py` 