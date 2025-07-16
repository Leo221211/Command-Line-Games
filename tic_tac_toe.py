"""
A simple command-line Tic-Tac-Toe game for two players.
Players take turns placing X or O on a 3x3 board.
The first player to get three in a row (horizontally, vertically, or diagonally) wins.
If the board fills up with no winner, it's a tie.
"""

def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    print("  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))

def check_winner(board):
    """Checks for a winner. Returns 'X', 'O', or None."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '.':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '.':
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '.':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '.':
        return board[0][2]
    return None

def tic_tac_toe():
    """Main game loop for the command-line Tic-Tac-Toe game."""
    board = [['.']*3 for _ in range(3)]
    player = 'X'
    moves_left = 9
    while True:
        print_board(board)
        print(f"{player}'s turn.")
        while True:
            try:
                move = input("Enter your move as 'row col': ")
                x, y = map(int, move.strip().split())
                if 0 <= x < 3 and 0 <= y < 3 and board[x][y] == '.':
                    board[x][y] = player
                    moves_left -= 1
                    break
                else:
                    print("Invalid move. Try again.")
            except Exception:
                print("Invalid input. Enter row and column numbers separated by space.")
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        if moves_left == 0:
            print_board(board)
            print("It's a tie!")
            break
        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe() 