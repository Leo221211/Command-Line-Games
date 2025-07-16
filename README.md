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

- Blackjack (21)

    - One player vs the dealer. Try to get as close to 21 as possible without going over.
    - Aces count as 1 or 11. Dealer hits until reaching 17 or more.
    - Standard 52-card deck. Simple ASCII output.
    - [Detailed rules from wikipedia](https://en.wikipedia.org/wiki/Blackjack)
    - Start playing: `python blackjack.py`

- Poker (Five Card Draw)

    - 2-4 human players. Each player is dealt 5 cards, can discard and draw new ones.
    - The best hand wins. Basic hand ranking (pair, two pair, three of a kind, straight, flush, full house, four of a kind, straight flush).
    - Standard 52-card deck. Simple ASCII output.
    - [Detailed rules from wikipedia](https://en.wikipedia.org/wiki/Five-card_draw)
    - Start playing: `python poker.py`

- Go Fish

    - 2-4 human players. Players ask each other for cards to collect books of four cards of the same rank.
    - If the asked player has the rank, they must give all cards of that rank; otherwise, the asker draws from the deck ('Go Fish').
    - The player with the most books at the end wins.
    - [Detailed rules from wikipedia](https://en.wikipedia.org/wiki/Go_Fish)
    - Start playing: `python go_fish.py` 