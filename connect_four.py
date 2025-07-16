"""
A simple command-line Connect Four game for two players.
Players take turns dropping pieces into a 7-column, 6-row board.
The first player to get four in a row (horizontally, vertically, or diagonally) wins.
If the board fills up with no winner, it's a tie.
"""

def print_board(board):
    """Prints the current state of the Connect Four board."""
    print("  " + " ".join(str(i) for i in range(7)))
    for row in board:
        print(" " + " ".join(row))

def valid_moves(board):
    """Returns a list of columns (indices) where a move can be made."""
    return [col for col in range(7) if board[0][col] == '.']

def make_move(board, col, player):
    """Drops a piece for the player into the specified column."""
    for row in reversed(board):
        if row[col] == '.':
            row[col] = player
            return True
    return False

def check_winner(board):
    """Checks for a winner. Returns 'X', 'O', or None."""
    rows, cols = 6, 7
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == '.':
                continue
            player = board[r][c]
            # Check horizontal
            if c <= cols - 4 and all(board[r][c+i] == player for i in range(4)):
                return player
            # Check vertical
            if r <= rows - 4 and all(board[r+i][c] == player for i in range(4)):
                return player
            # Check diagonal down-right
            if r <= rows - 4 and c <= cols - 4 and all(board[r+i][c+i] == player for i in range(4)):
                return player
            # Check diagonal up-right
            if r >= 3 and c <= cols - 4 and all(board[r-i][c+i] == player for i in range(4)):
                return player
    return None

def connect_four():
    """Main game loop for the command-line Connect Four game."""
    board = [['.']*7 for _ in range(6)]
    player = 'X'
    moves_left = 6 * 7
    while True:
        print_board(board)
        moves = valid_moves(board)
        if not moves:
            print("It's a tie!")
            break
        print(f"{player}'s turn. Valid columns: {moves}")
        while True:
            try:
                move = input("Enter the column (0-6) to drop your piece: ")
                col = int(move.strip())
                if col in moves:
                    make_move(board, col, player)
                    moves_left -= 1
                    break
                else:
                    print("Invalid move. Try again.")
            except Exception:
                print("Invalid input. Enter a column number (0-6).")
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    connect_four() 